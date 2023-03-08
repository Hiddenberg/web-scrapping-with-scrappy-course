import "../css/ProjectDescription.css"
function DocumentDescription() {
   return (
      <p className="project-description">
         This project shows information on some declassified documents taken directly from the official <strong><a href="https://www.cia.gov/readingroom/historical-collections" target="_blank">CIA historical-collections website</a></strong> along with their respective descriptions, images and links, the information was collected using the web-scrapper created in this repository.
      </p>
   );
}

export default DocumentDescription;