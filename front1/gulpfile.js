var gulp=require("gulp");
var css=require("gulp-cssnano");
var rename=require("gulp-rename");
var script=require("gulp-uglify");
var combine=require("gulp-concat");
var cache=require("gulp-cache");
var image_min = require('gulp-imagemin');
var bs = require('browser-sync');
var sass =require("gulp-sass");
var watch =require ("gulp-watch");

//设置路径
var path={
    "css":"./src/css/",
    "js":"./src/js/",
    "image":"./src/image/",
    "dist_css":"./dist/css/",
    "dist_js":"./dist/js/",
    "dist_image":"./dist/image/"
}

//压缩css文件
gulp.task("css",function () {
    gulp.src(path.css+"*.scss")
    .pipe( sass({"outputStyle":"compact"}).on("error",sass.logError))
        .pipe(css())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest(path.dist_css))
        .pipe(bs.stream())

});

//压缩js文件
gulp.task("script",function () {
    gulp.src(path.js+"*.js")
        .pipe(script())
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest(path.dist_js))


});

//结合文件
gulp.task("combine",function () {
    gulp.src([
        "./js/blog.js",
        "./js/index.js"
    ])
        .pipe(combine("combine.js"))
        .pipe(script())
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest("./dist/js"))
});

//压缩图片文件
gulp.task("image",function () {
    gulp.src(path.image+"*.*")
        .pipe(cache(image_min()))
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest(path.dist_image))
        .pipe(bs.stream())
});

//实时监听js,css,image的变化，更新到压缩文件中
gulp.task("watch",function () {
    watch(path.css+"*.scss",gulp.series('css'));
    watch(path.js+"*.js",gulp.series("script"));
    watch(path.image+"*.*",gulp.series("image"));

});

//初始化bowser-sync
gulp.task('browser-sync', function() {//注册任务
    bs.init({//调用API
        files: "**",//监听整个项目
        server: {
            baseDir: "./"  // 监听当前路径
        }
    });
});

//并行启动实时更新流浪其刷新，和压缩文件
gulp.task("default",gulp.series(gulp.parallel("watch","browser-sync")));//parallel并列执行函数


