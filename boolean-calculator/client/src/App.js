import './App.css';
import { Box, Grid, Container, TextField, Paper, Typography } from '@mui/material';
import React, { useState, useEffect } from 'react';
import TruthTable from './Table'
import axios from 'axios'
import { createTheme, ThemeProvider } from '@mui/material/styles';


axios.defaults.withCredentials = true


function App() {
  const [termData, setTermData] = useState({ inputTerm: '', variables: [], rowData: [] })

  useEffect(() => {
    sendSessionId()
  }, [])

  // Converts term array into JSON object to be sent via getRows() post request
  const toObject = term => {
    var obj = {}
    for (var i = 0; i < term.length; i++) {
      obj[i] = term[i]
    }
    return obj
  }

  // Starts Session with the Calculator backend via post request
  const sendSessionId = async () => {
    await axios.post('http://127.0.0.1:8000/api/set-session/', {
    }).then(function (response) {
      console.log(response)
    }).catch(function (error) {
      console.log(error);
    })
  }

  // Sends term data in JSON format to backend via post and recieves the calculated rows via get request and updates states with the received rows
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
          setTermData(prevTerm => ({ ...prevTerm, rowData: result.data }))
        })
      .catch((error) => { console.log(error) })
  }

  // Upon term being typed in the input field, the term is parsed and turned into JSON, sent to backend, and state updated with obtained data 
  const onChange = e => {
    var input = e.target.value.trim()
    var inputVariables = input.split(/[+*-]/).filter(i => i)
    var separatedInput = input.split(/([+*-])/).filter(i => i)
    var inputObj = toObject(separatedInput)
    setTermData(prevTerm => ({ ...prevTerm, inputTerm: input, variables: inputVariables }))
    getRows(inputObj)
  }

  // ########## STYLING ###########

  // Color palette
  let themePalette = createTheme({
    palette: {
      primary: {
        main: "#2962ff"
      },
      secondary: {
        main: "#768fff"
      },
      info: {
        main: "#0039cb"
      }
    },
  })

  // Component customizations
  const theme = createTheme(themePalette, {
    components: {
      MuiTableRow: {
        variants: [
          {
            props: { color: 'highlight' },
            style: {
              backgroundColor: themePalette.palette.primary.main
            }
          },
          {
            props: { color: 'body', type: "dark"},
            style: {
              backgroundColor: themePalette.palette.secondary.main,
              color: "white",
              "&:hover":{
                backgroundColor: themePalette.palette.primary.main
              }
            }
          },
          {
            props: { color: 'body', type: "light"},
            style: {
              backgroundColor: "white",
              "&:hover":{
                backgroundColor: themePalette.palette.primary.main,
                color: "white",
              }
            }
          }
        ]
      },
      MuiTypography: {
        variants: [
          {
            props: { type: "highlight" },
            style: {
              color: "white",
              fontWeight: "normal",
              fontSize: "large"
            }
          },
          {
            props: { type: "banner" },
            style: {
              color: "white",
              fontFamily: 'Poppins',
            }
          },
        ]
      },
      MuiPaper: {
        variants: [
          {
            props: { type: 'main' },
            style: {
              backgroundColor: "white",
              height: "100vh"
            }
          },
          {
            props: { type: 'banner' },
            style: {
              width: "100%",
              height: "62%",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              overflow: "hidden",
              backgroundColor: "#2962ff",
              marginTop: "5%",
              marginBottom: "3%"
            }
          }
        ]
      }
    }
  })

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <Paper type="main">
          <Box sx={{ height: '80vh', display: 'flex' }}>
            <Grid container spacing={0} sx={{ justifyContent: "center" }}>
              <Grid item xs={9}>
                <Paper elevation={3} type="banner">
                  <Typography variant='h1' type="banner">
                    BoolCalc
                  </Typography>
                </Paper>
              </Grid>
              <Grid item xs={11}>
                <Container maxWidth="false">
                  <TextField id="outlined-basic" label="Expression" variant="outlined" onChange={e => onChange(e)} value={termData.inputTerm} />
                  <TruthTable Term={{ termData }} />
                </Container>
              </Grid>
            </Grid>
          </Box>
        </Paper>
      </ThemeProvider>
    </div>
  );



}

export default App;
