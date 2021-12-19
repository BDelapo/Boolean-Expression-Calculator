import './App.css';
import { Box, Grid, Container, TextField } from '@mui/material';
import React, { useState, useEffect } from 'react';
import TruthTable from './Table'
import axios from 'axios'

axios.defaults.withCredentials = true


function App() {
  const [termData, setTermData] = useState({inputTerm: '', variables: [], rowData:[]})

  useEffect(() => {
    sendSessionId()
  }, [])


  const toObject = term => {
    var obj = {}
    for (var i = 0; i < term.length; i++) {
      obj[i] = term[i]
    }
    return obj
  }

  const sendSessionId = async () => {
    await axios.post('http://127.0.0.1:8000/api/set-session/', {
    }).then(function (response) {
      console.log(response)
    }).catch(function (error) {
      console.log(error);
    })
  }


  const getRows = async (input) => {
    
    await axios.post('http://127.0.0.1:8000/api/set-session/calculate/post', {
      term: input
    }).then(function (response) {
      console.log(response)
    }).catch(function (error) {
      console.log(error);
    })

    await axios.get('http://127.0.0.1:8000/api/set-session/calculate/get')
    .then(
      (result) => {
      console.log(result + 'hello')
       setTermData(prevTerm => ({...prevTerm, rowData: result.data}))
    })
    .catch((error) => {console.log(error)})
  }

  const onChange = e => {
    var input = e.target.value
    var inputVariables = input.split(/[+*-]/)
    var separatedInput = input.split(/([+*-])/)
    var inputObj = toObject(separatedInput)
    getRows(inputObj)
    setTermData(prevTerm => ({...prevTerm, inputTerm: input, variables : inputVariables}))
  }

  console.log(termData.inputTerm)

  return (
    <div className="App">
      <Box sx={{ height: '100vh', display: 'flex', alignItems: 'center' }}>
        <Grid container spacing={0}>
          <Grid item xs={12}>
            <Container maxWidth="sm">
              <TextField id="outlined-basic" label="Outlined" variant="outlined" onChange={e => onChange(e)} value={termData.inputTerm} />
            </Container>
          </Grid>
          <Grid item xs={12}>
            <Container maxWidth="sm">
              <TruthTable Term={{ termData }} />
            </Container>
          </Grid>
        </Grid>
      </Box>
    </div>
  );
}

export default App;
