import React, { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPlus } from "@fortawesome/free-solid-svg-icons";
import "./FileUpload.css";

import { preparedImage } from "../../api/api";

const FileUpload = ({ files, setFiles, removeFile }) => {

  const [arquivo, setArquivo] = useState("")
 
  const uploadFiles = async (e) => {
    e.preventDefault();
    console.log("aqui");
    console.log(arquivo, typeof(arquivo));
    const result = await preparedImage(arquivo);
  };

  return (
    <>
      <div className="file-card">
        <form onSubmit={uploadFiles}>
          <div className="file-inputs">
            <input
              type="text"
              id="meuArquivo"
              name="arquivo"
              onChange={(e) => setArquivo(e.target.value)}
            />
            {/* <button type="submit">
              <i>
                <FontAwesomeIcon icon={faPlus} />
              </i>
              Upload
            </button> */}
          </div>
          <p className="main">Supported files</p>
          <p className="info">JPG, PNG</p>
          <input type="submit" value="Submit" />
        </form>
      </div>
    </>
  );
};

export default FileUpload;
