import "../css/DocumentItem.css"
function DocumentItem({imageUrl, title, description, link}) {
   return (
      <div className="document-item">
         <div className="document__image-wrapper">
            <img className="document__image" src={imageUrl || "https://images.pexels.com/photos/261679/pexels-photo-261679.jpeg"} />
            <h2 className="document__title"><a href={link} target="_blank">{title}</a></h2>
         </div>
         <p className="document__description" title={description}>{description}</p>
      </div>
   );
}

export default DocumentItem;