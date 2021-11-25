import { DataGrid } from '@mui/x-data-grid'

const Table = (props) => {

    const column = props.Term.termData.separatedTerm.map((term, id) => {

        return {field: id, headerName: term, width: 70 }
    
    })


    const rowDataValues = Object.values(props.Term.termData.rowData)

    const rows = rowDataValues.map((row, id)=> {
        return {id: id, row}
    })

    console.log(rows)

    return (
        <div>
            <DataGrid
                rows={rows}
                columns={column}
                rowHeight={38}
                checkboxSelection
                disableSelectionOnClick
            />
        </div>
    )

}


export default Table