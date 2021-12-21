import { Table, TableContainer, TableHead, TableBody, TableRow, TableCell, Paper, Typography } from '@mui/material';



const TruthTable = (props) => {

    // Maps the header values from props
    const VariableColumns = props.Term.termData.variables.map((term, key) => {
        return (
            <TableCell align="center" sx={{ width: 30 }} key={key}>
                <Typography type="highlight">{term}</Typography>
            </TableCell>)
    })

    // Turns the rows obtained from backend into an array
    const rowDataValues = Object.values(props.Term.termData.rowData)

    // Maps the rows array values from props
    const Rows = rowDataValues.map((row, key) => {
        const rowItemValues = Object.values(row)
        const RowItems = rowItemValues.map((rowItem, key) => {
            return <TableCell align="center" sx={{ width: 30, color: "inherit" }} key={key}>{rowItem}</TableCell>
        })
        return (
            key % 2 === 1 ?
                <TableRow color="body" type="dark" key={key}> {RowItems} </TableRow>
                : 
                <TableRow color="body" type="light" key={key} >{RowItems}</TableRow>)
    })

    return (
        <Paper sx={{ width: "100%", overflow: "hidden", margin: 1 }}>
            <TableContainer sx={{ maxHeight: "60vh" }}>
                <Table sx={{ minWidth: "650px" }} aria-label="simple table">
                    <TableHead>
                        <TableRow color="highlight">
                            {VariableColumns}
                        </TableRow>
                    </TableHead>
                    <TableBody>
                        {Rows}
                    </TableBody>
                </Table>
            </TableContainer>
        </Paper>
    )

}


export default TruthTable