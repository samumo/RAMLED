var btn = document.getElementById("buttonId");


var name_mask = JSON.stringify({"fade": 0.3, "auto_off": 1, "name_mask": ["test_1"]})

// btn.addEventListener('click', async _ => {
//   try {     
//     const response = await fetch('http://192.168.0.100:8080/api/v1.0/set_name_mask', {
//       method: 'post',
//       url: 'http://192.168.0.100:8080/api/v1.0/set_name_mask',
//       data: name_mask,
//       contentType: 'application/json; charset=UTF-8',
//       // body: {
//       //   "fade": 0.3, "auto_off": 1, "name_mask": ["test_1"]
//       // }
//     });
//     console.log('Completed!', response);
//   } catch(err) {
//     console.error(`Error: ${err}`);
//   }
// });

// (function($){
//   function set_name_mask( e ){
//       $.ajax({
//           url: 'http://192.168.0.100:8080/api/v1.0/set_name_mask',
//           dataType: 'text',
//           type: 'post',
//           contentType: 'application/json; charset=UTF-8',
//           data: name_mask,
//           success: function( data ){
//             console.log(data);
//           },
//           error: 
//               console.log( errorThrown ),
          
//       });

//       e.preventDefault();
//   }

//   $('#button1').addEventListener("click", set_name_mask);
// })(jQuery);