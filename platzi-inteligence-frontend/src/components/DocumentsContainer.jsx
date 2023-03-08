import "../css/DocumentsContainer.css"
import data from "../assets/cia.json"
import DocumentItem from "./DocumentItem";
import { useState } from "react";
import { useMemo } from "react";

function DocumentsContainer() {
   const [search, setSearch] = useState("")
   const sortedData = data.sort((a, b) => a.image && !b.image ? -1 : 1)


   const filteredItems = useMemo(() => 
      sortedData.filter(item => item.title.toLowerCase().includes(search.toLowerCase()))
      ,[search]
   )


   return (
      <div className="documents">
         <div className="documents__search-bar">
            <input onChange={(ev) => {setSearch(ev.target.value)}} className="documents__search-bar__input" type="text" placeholder="Search"/>
         </div>
         <div className="documents-container">
            {filteredItems.length > 0 ? 
               filteredItems.map(({body, image, title, url}) => (
                  <DocumentItem key={title} imageUrl={image} title={title} description={body.join(" ")} link={url} />
               )) :
               <h2>No results found</h2>
            }
         </div>
      </div>
   );
}

export default DocumentsContainer;