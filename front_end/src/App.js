import React, {useState} from "react";

import Classe from "./Components/Classe";
import ListaArquivo from "./Components/Lista_arquivo";
import Resultado from "./Components/Resultados";
import Titulo from "./Components/Titulo"
import FileUpload from "./Components/FileUpload";
import FileList from "./Components/FileList";

import uploadArq from "./api/api"

import './App.css'

export default function App() {
  const [files, setFiles] = useState([]);

  const removeFile = (filename) => {
    setFiles(files.filter((file) => file.name !== filename));
  };

  const dowloadFile = async (event) => {
    const file = event.target.files[0];
    const formData = new FormData();
    formData.append("newFile", file, file.name);

    axios.post("http://localhost:8080/arquivos", formData);
  }

  return (
    <div className="first">
      <div className="container">
        <Titulo />
        <Classe />
        {/* <form   action="http://localhost:8080/arquivos" 
                method="POST" 
                enctype="multipart/form-data">
            <label for="meuArquivo">Upload Arquivo</label>
            <input type="file" id="meuArquivo" name="meuArquivo"/>
            <input type="submit" value="Submit"/>
        </form> */}
        {/* <ListaArquivo /> */}
        {/* <Resultado /> */}
        <FileUpload files={files} setFiles={setFiles} removeFile={removeFile} />
        <FileList files={files} removeFile={removeFile} />
      </div>
    </div>
  );
}
