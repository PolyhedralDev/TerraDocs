'use strict';

const gulp = require('gulp');
const pluginerror = require('plugin-error');
const browsersync = require('browser-sync').create();
const del = require('del');
const spawn = require('child_process').spawn;

const docsDir = "docs";
const ignoredPaths = [
    "config/documentation/objects",
    "config/documentation/files",
    "install/versions.rst",
    "install/versions/platforms",
]

function shell(plugin, command, args) {
    return (done) =>
        spawn(command, args, {stdio: 'inherit'})
            .on('error', (err) => {
                done(new pluginerror(plugin, err))
            })
            .on('exit', (code) => {
                if (code === 0) {
                    // Process completed successfully
                    done()
                } else {
                    done(new pluginerror(plugin, `Process failed with exit code ${code}`));
                }
            })
}

function webserver(done) {
    browsersync.init({
        watch: true,
        server: "./build/dev/html/"
    }, function () { this.server.on('close', done) })
}


function watch() {
    gulp.watch([`./${docsDir}/**`, ...ignoredPaths.map(dir => `!./${docsDir}/${dir}`)], gulp.series('sphinx:dev'));
}

gulp.task('clean', () => del(['build']));

gulp.task('sphinx', shell(
    'sphinx', 'sphinx-build', ['-W', '-d', 'build/doctrees', docsDir, 'build/html']
));

gulp.task('sphinx:dev', shell(
    'sphinx', 'sphinx-build', [docsDir, 'build/dev/html']
));

gulp.task('build', gulp.series('clean', 'sphinx'));
gulp.task('build:dev', gulp.series('clean', 'sphinx:dev'));

gulp.task('default', gulp.series('build:dev', gulp.parallel(webserver, watch)));
