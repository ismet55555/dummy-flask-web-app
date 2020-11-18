// Create a XMLHttpRequest object to handle REST calls
// TODO: Switch to fetch API!
let request = new XMLHttpRequest();  


///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////


// Reset and clear all components on the page
// window.onload = clear_and_reset_all()


///////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////


function http_request_helper(method, ip, port, endpoint, args_dict){
    ////////////////////////////////////////////////
    // Usage:
    //      GET
    //          let time = http_request_helper('GET', picell_ip, '5000', 'get_time')
    //      POST
    //          let response = http_request_helper('POST', null, '', apc_on_off, {'fixture_euid':fixture_euid_selected})
    ////////////////////////////////////////////////

    // Adding any passed arguments in key:value dict format
    argText = ''
    if (args_dict != null){
        argText += '?'
        for(let key in args_dict){
            let value = args_dict[key]
            argText = argText + key + '=' + value + '&'
        }
    }
    argText = argText.substring(0, argText.length - 1);

    // Forming the request
    if (ip != null){
        // Sending request to remote location (picell)
        request_url = 'http://' + ip + ':' + port + '/' + endpoint + argText
    } else {
        // Sending request to local flask server
        request_url = endpoint + argText
    }
    console.log('Sending Request: ' + request_url)

    // Sending the request
    try {
        request.open(method.toUpperCase(), request_url, false);
        request.setRequestHeader('Access-Control-Allow-Origin', '*')
        request.send();
        return request.responseText;
    } catch(error) {
        console.warn("ERROR: Failed to send request. Response: " + error)
        return null;
    }
    
}


///////////////////////////////////////////////////////////////////////////////////////////////////


function start_slideshow() {
    // Starting the image slideshow
    let response = http_request_helper('POST', null, 5555, 'endpoint_1')
}

function stop_slideshow() {
    // Stopping the image slideshow
    let response = http_request_helper('POST', null, 5555, 'endpoint_2')
}

