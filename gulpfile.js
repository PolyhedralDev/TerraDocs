'use strict';

import gulp from 'gulp';
import pluginerror from 'plugin-error';
import browsersync from 'browser-sync';
import {deleteAsync} from 'del';
import { spawn } from 'child_process';

const docsDir = "docs";
const ignoredPaths = [
    "config/documentation/objects",
    "config/documentation/configs",
    "install/versions.rst",
    "install/versions/platforms",
];

function shell(plugin, command, args) {
    return (done) => {
        const child = spawn(command, args, { stdio: 'inherit' });

        child.on('error', (err) => {
            done(new pluginerror(plugin, err));
        });

        child.on('exit', (code) => {
            if (code === 0) {
                // Process completed successfully
                done();
            } else {
                done(new pluginerror(plugin, `Process failed with exit code ${code}`));
            }
        });
    };
}

function webserver(done) {
    const server = browsersync.create();

    server.init({
        watch: true,
        server: "./build/dev/html/"
    }, function () {
        this.server.on('close', done);
    });
}

function watch() {
    gulp.watch([`./${docsDir}/**`, ...ignoredPaths.map(dir => `!./${docsDir}/${dir}`)], gulp.series('sphinx:dev'));
}

gulp.task('clean', () => deleteAsync(['build']));

gulp.task('sphinx', shell(
    'sphinx', 'sphinx-build', ['-W', '-d', 'build/doctrees', docsDir, 'build/html']
));

gulp.task('sphinx:dev', shell(
    'sphinx', 'sphinx-build', [docsDir, 'build/dev/html']
));

gulp.task('build', gulp.series('clean', 'sphinx'));
gulp.task('build:dev', gulp.series('clean', 'sphinx:dev'));

gulp.task('default', gulp.series('build:dev', gulp.parallel(webserver, watch)));
