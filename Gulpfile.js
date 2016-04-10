'use strict';

var path = require('path');
var gulp = require('gulp');
var sass = require('gulp-sass');
var bourbon = require('bourbon');
var neat = require('bourbon-neat');
var autoprefixer = require('gulp-autoprefixer');


var sass_src = 'src/modelbouwdag/sass/**/*.scss';
var css_dir = 'src/modelbouwdag/static/modelbouwdag/css';


gulp.task('sass', function() {
    gulp.src(sass_src)
        .pipe(sass({
            // sourceMap: true, // requires extra plugin
            outputStyle: 'expanded',
            includePaths: bourbon.includePaths.concat(neat.includePaths)
        }).on('error', sass.logError))
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))
        .pipe(gulp.dest(css_dir));
});


// watch task
gulp.task('default',function() {
    gulp.watch(sass_src, ['sass']);
});
