var btn = document.getElementById("buttonId");

btn.addEventListener('click', async _ => {
  try {     
    const response = await fetch('http://192.168.0.100:8080/api/v1.0/set_name_mask', {
      method: 'post',
      body: {
        "fade": 0.3, "auto_off": .5, "name_mask": ["B2.GF"]
      }
    });
    console.log('Completed!', response);
  } catch(err) {
    console.error(`Error: ${err}`);
  }
});