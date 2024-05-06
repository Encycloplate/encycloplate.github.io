function htmlTableOfContents(documentRef, container) {
    var documentRef = documentRef || document;
    var headings = [].slice.call(documentRef.body.querySelectorAll('article h1, article h2, article h3, article h4, article h5, article h6'));
    var parentH2 = null;

    var toc = document.createElement('div');
    toc.id = 'toc';

    headings.forEach(function(heading, index) {
        var anchor = documentRef.createElement('a');
        anchor.setAttribute('name', 'toc' + index);
        anchor.setAttribute('id', 'toc' + index);

        var link = documentRef.createElement('a');
        link.setAttribute('href', '#toc' + index);
        link.textContent = heading.textContent;

        var div = documentRef.createElement('div');
        var tagName = heading.tagName.toLowerCase();
        div.setAttribute('class', tagName);

        if (tagName === 'h2') {
            parentH2 = heading;
        }

        if (tagName === 'h3' && parentH2) {
            div.style.marginLeft = '20px';
        }

        if (tagName === 'h1') {
            div.style.fontWeight = 'bold';
        }

        div.appendChild(link);
        toc.appendChild(div);
        heading.parentNode.insertBefore(anchor, heading);
    });

    container.appendChild(toc);
}

function informtoc() {
    var popupDiv = document.createElement('div');
    popupDiv.classList.add('popup');

    // styling the div
    popupDiv.style.position = 'fixed';
    popupDiv.style.top = '50%';
    popupDiv.style.left = '50%';
    popupDiv.style.transform = 'translate(-50%, -50%)';
    popupDiv.style.zIndex = '1000';

    // adding text
    var textNode = document.createElement('h2');
    textNode.textContent = "Table of Contents";
    textNode.onclick = function() {
        document.body.removeChild(popupDiv);
    };
    popupDiv.appendChild(textNode);

    // create container for table of contents
    var tocContainer = document.createElement('div');
    popupDiv.appendChild(tocContainer);

    // call the table of contents function
    htmlTableOfContents(document, tocContainer);

    // appending it
    document.body.appendChild(popupDiv);
}
