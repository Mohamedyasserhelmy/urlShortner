import './App.css';
import React, { useState } from 'react';
import './form.css'


function App() {
  const [inputValue, setInputValue] = useState('');
  const handleSubmit = (event) => {
    event.preventDefault();

    // Send the input value to Flask endpoint here using fetch()
    fetch('http://127.0.0.1:5000/submitUrl', {
      method: 'POST',
      body: JSON.stringify({ inputValue }),
      headers: {
        'Content-Type': 'application/json'
      },
      crossorigin: 'anonymous',
     
    }).then(response => {
      console.log(response);
    })
  }

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  }
  
 
  return (
    <form onSubmit={handleSubmit}>
      <label>
        Enter URL : <span></span>
        <input type="text" value={inputValue} onChange={handleInputChange} required />
      </label>
      <button type="submit">Shorten</button>
    </form>
    
  );
}




export default App;
