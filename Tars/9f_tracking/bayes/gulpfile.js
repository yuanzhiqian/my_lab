var gulp = require('gulp');
var path = require('path');
var package = require('./package.json')
$ = require('gulp-load-plugins')();

gulp.task('clean', function() {
  return gulp.src('./dist', {
    read: false
  }).pipe($.rimraf({
    force: true
  }))
})

gulp.task('js', ['clean'], function() {
  return gulp.src('./scripts/bayes.js')
    .pipe(gulp.dest('./dist'))
    .pipe($.uglify())
    .pipe($.rename({
      extname: '-' + package.version + '.min.js'
    })
  )
  .pipe(gulp.dest('./dist'))
})

gulp.task('default', ['js'])
