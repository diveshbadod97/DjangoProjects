import React, {useRef, useState} from 'react';
import {SketchField, Tools} from 'react-sketch';
import {Button, Alert} from 'react-bootstrap'
import {saveAs} from 'file-saver'
import axios from 'axios'
const styles={
    draw: {
        margin : '0 auto'
    }
}

const Draw = () =>{
    const [send, setSend] = useState(false)
    const [result, setResult] = useState()
    const sketch = useRef()
    const handleSubmit = () =>{
        const canvas = sketch.current.toDataURL()
        // saveAs(canvas, 'digit.jpg')
        sendData(canvas)
    }
    const handleReset = () => {
        sketch.current.clear()
        sketch.current._backgroundColor('black')
        setSend(false)
        setResult()
    }

    const sendData = (c) =>{
        const headers = {
            'accept': 'application/json'
        }
        const fd = new FormData()
        fd.append('image', c)
        axios.post('http://127.0.0.1:8000/api/digits/', fd, {headers:headers})
        .then(res=>{
            console.log(res.data);
            setSend(true)
            getImageResult(res.data.id)
        })
        .catch(err=>{
            console.log(err);  
        })
    }
    const getImageResult = (id) =>{
        axios.get(`http://127.0.0.1:8000/api/digits/${id}`)
        .then(res=>{
            setResult(res.data.result)
        })
    } 
    return (
        <React.Fragment>
            {send && <Alert variant="info">Successfully saved for classification</Alert>}
            {result && <h3>Result is {result}</h3>}
            <SketchField 
            ref={sketch}
            width='800px' 
            height='800px' 
            tool={Tools.pencil}
            backgroundColor='black'
            lineColor='white'
            imageFormat='jpg'
            lineWidth={60}
            style={styles.draw}/>
            <div className="mt-3">
                <Button onClick={handleSubmit} variant="primary">Send</Button>
                <Button onClick={handleReset} variant="secondary">Reset</Button>
            </div>
        </React.Fragment>
    )
}
export default Draw;

