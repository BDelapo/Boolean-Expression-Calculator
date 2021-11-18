import { DataGrid } from '@mui/x-data-grid'

const Table = (props) => {

    const column = props.Term.separatedTerm.map( (term, id) => {

        return {field: id, headerName: term, width: 70 }
    
    })


    const rows = [{id: 1, term: props.Term.separatedTerm}]

    const columns = [{ field: 1, headerName: props.Term.separatedTerm, width: 70 }, { field: 2, headerName: props.Term.separatedTerm, width: 70 }]

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