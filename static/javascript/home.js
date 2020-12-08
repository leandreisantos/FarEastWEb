window.addEventListener('scroll',()=>{
  const scrolled = window.scrollY;
  const level=1160;

  if (scrolled>level){
    const counters= document.querySelectorAll('.counter');
    counters.forEach(counter =>{
         const updateCount =() => {
         const target = +counter.getAttribute('data-target');
         const count= +counter.innerText;

         const inc =1;
         if (count<target){
            var x=count+inc
            counter.innerText=x;
            setTimeout(updateCount,180);
         }else{
           count.innerText=target;
         }
       }
       updateCount();
    });
  }
  if (scrolled>level){
    const counters= document.querySelectorAll('.counter2');
    counters.forEach(counter =>{
         const updateCount =() => {
         const target = +counter.getAttribute('data-target');
         const count= +counter.innerText;

         const inc =1;
         if (count<target){
            var x=count+inc
            counter.innerText=x;
            setTimeout(updateCount,80);
         }else{
           count.innerText=target;
         }
       }
       updateCount();
    });
  }
  if (scrolled>level){
    const counters= document.querySelectorAll('.counter3');
    counters.forEach(counter =>{
         const updateCount =() => {
         const target = +counter.getAttribute('data-target');
         const count= +counter.innerText;

         const inc =1;
         if (count<target){
            var x=count+inc
            counter.innerText=x;
            setTimeout(updateCount,100);
         }else{
           count.innerText=target;
         }
       }
       updateCount();
    });
  }
  if (scrolled>level){
    const counters= document.querySelectorAll('.counter4');
    counters.forEach(counter =>{
         const updateCount =() => {
         const target = +counter.getAttribute('data-target');
         const count= +counter.innerText;

         const inc=1;
         if (count<target){
            var x=(count+inc+13)
            counter.innerText=x;
            setTimeout(updateCount,1);
         }else{
           count.innerText=target;
         }
       }
       updateCount();
    });
  }
});

$(document).ready(function() {
  // executes when HTML-Document is loaded and DOM is ready


  /*
  ################
  Add navbar background color when scrolled
  */
  $(window).scroll(function() {
    if ($(window).scrollTop() > 56) {
      $(".navbar").addClass("bg-light");
      $(".navbar").removeClass("navbar-dark");
      $(".navbar").addClass("navbar-light");
      $(".navbar").css("padding","10px")
      $(".navbar").css("box-shadow","0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)")
    } else {
      $(".navbar").removeClass("bg-light");
      $(".navbar").removeClass("navbar-light");
      $(".navbar").addClass("navbar-dark");
      $(".navbar").css("padding","50px")
      $(".navbar").css("box-shadow","0 0px 0px 0 rgba(0, 0, 0, 0.2), 0 0px 0px 0 rgba(0, 0, 0, 0.19)")
    }
  });
  // If Mobile, add background color when toggler is clicked
  $(".navbar-toggler").click(function() {
    if (!$(".navbar-collapse").hasClass("show")) {
      $(".navbar").addClass("bg-dark");
    } else {
      if ($(window).scrollTop() < 56) {
        $(".navbar").removeClass("bg-dark");
      } else {
      }
    }
  });
  // ############

  // document ready
});
