import './App.css';
import { Box, Grid, Container, TextField } from '@mui/material';
import React, { useState, useEffect } from 'react';
import Table from './Table'
import axios from 'axios'





function App() {
  const [inputTerm, setInputTerm] = useState('')
  const [separatedTerm, setSeparatedTerm] = useState([])


  const toObject = term =>{
    var obj = {}
    for(var i = 0; i < term.length; i++){
      obj[i] = term[i]
    }
    return obj
  }

  

  const getRows = async (input) => {

    await axios.post('http://127.0.0.1:5000/calculator', {
      term : input
    }).then(function (response) {
      console.log(response);
    }).catch(function (error) {
      console.log(error);
    })
    
    axios.get('http://127.0.0.1:5000/calculator')
    .then((response) => {
      console.log(response.data);
    })
    
  }

  const onChange = e => {
    var input = e.target.value
    var separatedInput = input.split(/([+*\/-])/)
    setInputTerm(input)
    setSeparatedTerm(separatedInput)
  
    var inputObj = toObject(separatedInput)
    getRows(inputObj)
    
  }



  return (
    <div className="App">
      <Box sx={{ height: '100vh', display: 'flex', alignItems: 'center' }}>
        <Grid container spacing={0}>
          <Grid item xs={12}>
            <Container maxWidth="sm">
              <TextField id="outlined-basic" label="Outlined" variant="outlined" onChange={e => onChange(e)} value={inputTerm} />
            </Container>
          </Grid>
          <Grid item xs={12}>
            <Container maxWidth="sm">
              <Table Term={{ separatedTerm }} />
            </Container>
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default App;
