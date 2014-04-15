$(function(){
		   
		   
		    $(".info p").each(function(){
					var txt = $(this).parent().siblings().attr("src");
					$(this).html(txt);
			})
			
		   $(".menuprincipal li").click(function(){
				var index = $(this).index();
			   $(this).addClass("current").siblings().removeClass("current");
		       $(".content li").eq(index).show().siblings().hide();
		    })
			
		
		
		   $(".menuDescCont li").click(function(){
				var index = $(this).index();
			   $(this).addClass("current").siblings().removeClass("current");
		       $(".contentDescCont li").eq(index).show().siblings().hide();
		    })
		    
			
			$(".MenuCarSer li").click(function(){
			var index = $(this).index();
			   $(this).addClass("current").siblings().removeClass("current");
		       $(".contentCarSer li").eq(index).show().siblings().hide();
		    })
			
			
})