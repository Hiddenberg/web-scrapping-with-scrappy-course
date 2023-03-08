import DocumentsContainer from "./components/DocumentsContainer.jsx"
import Header from "./components/Header.jsx"
import DocumentDescription from "./components/ProjectDescription.jsx"

import "./App.css"
function App() {
   return (
      <div className="App">
         <Header />
         <DocumentDescription />
         <DocumentsContainer />
      </div>
   )
}

export default App
