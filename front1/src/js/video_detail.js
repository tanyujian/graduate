function Comment() {
    this.submit_btn=$("#submit-btn");
    this.comment_box=$(".comment-box");
    this.btn_file=$("#work-file");
    this.send_file=$(".send-work");
    this.cancel=$("#cancel");
}


Comment.prototype.run=function () {
    this.listenComment();
    this.initPlayer();
    this.listenFile();
    this.listenCancel();
};

Comment.prototype.reply=function (reply_id) {
    var reply=$("#comment-content");
    reply.attr("reply-id",reply_id);
    $('html').animate({scrollTop:$('#comment-content').offset().top - 90},300,function () {
            // CKEDITOR.instances['id_context'].focus();

        });
};
Comment.prototype.listenComment=function () {
    var self=this;
    self.submit_btn.click(function () {
        var html=$("#comment-content");
        var content=html.val();
        var reply_id=html.attr("reply-id");
        var object_id=html.attr("object-id");
        var content_object=html.attr("content-object");
        Ajax({
            url:"/comment/",
            type:"POST",
            data:{"object_id":object_id,"content":content,"reply_id":reply_id,
            "content_type":content_object},
            cache:false,
            success:function (data) {
                if (data["code"]===200){
                    if(reply_id==0){
                        console.log(data["data"]);
                        var html1=template("comment-model",data=data["data"]);
                        self.comment_box.prepend(html1);
                    }
                    else{
                         console.log("错误啊1");
                         console.log(data["data"]["root"]["id"]);
                         var id=data["data"]["root"]["id"];
                        var html1=template("reply-model",data=data["data"]);
                        $("#comment-matter-"+id).append(html1);
                            html.attr("reply-id",0)
                    }

                }
                else{
                    console.log("错误啊");
                }
            }

        });

    });
};

Comment.prototype.listenFile=function () {
    var self =this;
    self.btn_file.click(function () {
        self.send_file.show();
    })
};

Comment.prototype.listenCancel=function () {
    var self=this;
    self.cancel.click(function () {
        event.preventDefault();
        self.send_file.hide()
    })
};

Comment.prototype.initPlayer = function () {
    var videoInfoSpan = $("#video-info");
    var video_url = videoInfoSpan.attr("data-video-url");
    var cover_url = videoInfoSpan.attr("data-video-cover");
    // var course_id = videoInfoSpan.attr('data-course-id');
    console.log("hahahahaha");
    var player = cyberplayer("playercontainer").setup({
            width: '100%',
            height: '100%',
            file: video_url,
            image: cover_url,
            autostart: false,
            stretching: "uniform",
            repeat: false,
            volume: 100,
            controls: true,
            tokenEncrypt: true,
            // AccessKey
            ak:"efc4ef4802ff498b9c3b5cb73098a48a"
            // ak:"08bfd1fc1b6b48ecb21267b447491226"
        });

        player.on('beforePlay',function (e) {
            if(!/m3u8/.test(e.file)){
                return;
            }
            Ajax({
                url: '/course/token/',
                type:"GET",
                data: {
                    'video': video_url
                    // 'course_id': course_id
                },
                cache:false,
                success: function (data) {
                    if(data["code"] === 200){
                        var token = data['data'];
                        console.log(data["data"]);
                        player.setToken(e.file,token);
                    }else{
                         console.log(data['message']);
                        player.stop();
                    }
                },
                fail: function (error) {
                    console.log(error);
                }
            });
        });
};

$(function () {
   var comment=new Comment();
   comment.run();
});