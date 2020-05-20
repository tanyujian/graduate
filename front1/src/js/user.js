function UserUnitl() {
 this.send_code=$("#send_code");
 this.username=$("#username");
 this.person=$(".user-more-box");
 this.search=$(".search-li");
 this.search_1=$(".search");
}

UserUnitl.prototype.run=function () {
    this.captcha();
    this.sendEmail();
    this.listen_username();
    this.listenSearch();

};

UserUnitl.prototype.captcha=function(){
        $('img.captcha').click(function() {
        $.getJSON('/captcha/refresh/',function(json) {
            // This should update your captcha image src and captcha hidden input
            console.log(json);
            $("img.captcha").attr("src",json.image_url);
            $("#id_captcha_0").val(json.key);
        });
        return false;
    });
};

UserUnitl.prototype.sendEmail=function () {
    var self=this;
     self.send_code.off().click(function () {
         event.preventDefault();
        var email=$("#id_email").val();
        if(email== "") {
            $("#tip").text("邮件不能为空");
            return false;
        }
        console.log(email);
        $.ajax({
            url:"/teacher/sendemail/",
            type:"GET",
            data:{"email":email},
            cache:false,
            success:function(data){
                $("#tip").text(data["success"]);
                console.log("12345")
        }

        });
            $(this).addClass("disabled");
            $(this).attr("disabled",true);
            var time=5;
            self.send_code.text(time+"s");
            var interval=setInterval( function(){
                if(time<= 0){
                    clearInterval(interval);//清除变量
                    self.send_code.removeClass("disabled");
                    self.send_code.attr("disabled",false);
                    self.send_code.text("发送验证码");
                    return true;
                }
                time--;
                 console.log("123456");
                self.send_code.text(time+"s");
            },1000);
            });
};

UserUnitl.prototype.listen_username=function () {
    var self=this;
    console.log("Dasd");
    this.username.hover(function () {
        self.person.show();
        console.log("dadsa");
    },function () {
        self.person.hide();
    });
};

UserUnitl.prototype.listenSearch=function () {
    var self=this;
    self.search.hover(function () {
        self.search_1.show();
    },function () {
        self.search_1.hide();
    })
};

$(function () {
    var user=new UserUnitl();
    user.run();
});