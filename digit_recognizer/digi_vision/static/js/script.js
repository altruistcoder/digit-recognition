// const video = document.getElementById('player');
// const canvas = document.getElementById('photo');
// const ctx = canvas.getContext('2d');
// const strip = document.getElementById('strip');
//
// function getVideo(){
//    navigator.mediaDevices.getUserMedia({
//        video:true,
//        audio:false
//    })
//        .then((stream)=> {
//            video.src = window.URL.createObjectURL(stream);
//            video.play();
//        })
//        .catch(err =>{
//            window.alert("WEBCAM ACCESS DENIED");
//        })
// }
//
// function paintToCanvas(){
//    const width = video.videoWidth;
//    const height = video.videoHeight;
//    console.log(width,height)
//
//    setInterval(()=>{
//        ctx.drawImage(video,0,0,width,height);
//    },16)
// }
//
// function takePhoto(){
//    const data = canvas.toDataURL('/image/jpeg'); //base 64. representation of photo
//    // console.log(data);
//    setInterval(function(){
//        $.post(
//            '/',
//            {data:data},
//            (value)=>{
//                console.log(value)
//            }
//        )
//    },300)
//
//    // let link = document.createElement('a');
//    // link.href = data;
//    // link.setAttribute('download','img')
//    // link.textContent = "Click Me";
//    // strip.insertBefore(link, strip.firstChild)
// }
//
// getVideo();

// function paintFunction(){
//    paintToCanvas();
//    takePhoto()
// }