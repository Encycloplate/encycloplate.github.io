function inform(text) {
    var popupDiv = document.createElement('div');
    popupDiv.classList.add('popup');

    // styling the div
    popupDiv.style.position = 'fixed';
    popupDiv.style.top = '50%';
    popupDiv.style.left = '50%';
    popupDiv.style.transform = 'translate(-50%, -50%)';
    popupDiv.style.zIndex = '1000';

    // adding text
    var textNode = document.createTextNode(text);
    popupDiv.appendChild(textNode);
    
    // close button
    var closeButton = document.createElement('button');
    closeButton.textContent = 'OK';
    closeButton.onclick = function() {
        document.body.removeChild(popupDiv);
    };
    popupDiv.appendChild(closeButton);

    // appending it
    document.body.appendChild(popupDiv);
}
