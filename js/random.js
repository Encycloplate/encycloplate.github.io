function fetchDirectoryList(directoryPath, callback) {
  fetch(directoryPath)
      .then(response => response.text())
      .then(html => {
          const parser = new DOMParser();
          const doc = parser.parseFromString(html, 'text/html');
          const links = Array.from(doc.querySelectorAll('a[href]'));
          const fileList = links.map(link => link.getAttribute('href'));
          callback(fileList);
      })
      .catch(error => console.error('Error fetching directory list:', error));
}

function redirectToRandomPage(directoryList) {
  const randomIndex = Math.floor(Math.random() * directoryList.length);
  const randomPage = directoryList[randomIndex];
  const rootPath = window.location.origin;
  window.location.href = rootPath + '/a/' + randomPage;
}

fetchDirectoryList('/a/', redirectToRandomPage);