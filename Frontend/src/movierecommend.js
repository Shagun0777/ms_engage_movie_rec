import "./App.css";
import Axios from "axios";
// import Header from "./components/Header";
import React, { useState, useEffect } from "react";
import ExpandableList from "./components/ExpandableList";

import {useParams, BrowserRouter as Router, Route, Switch} from 'react-router-dom'
// "logged user": "",
// "watched": [],
// "recommended_movies": [],
// "status": "User does not exist visit http://localhost:8000/create_user/?user_id=raja",
// "register here": "http://localhost:8000/create_user/?user_id=raja"


const Recommend = ({ params }) => {
  let { id } = useParams();
  console.log('id is',id, params)

  let [exact_match, setExact] = useState([])
  let [recommend_by_name, setName] = useState([])
  let [recommend_by_genre, setGenre] = useState([])
  let [recommend_by_cast, setCast] = useState([])
  let [recommend_final, setFinal] = useState([])
//   let [, setScraps] = useState([]);


  useEffect(() => {
    fetchScraps();

  }, []);

  const fetchScraps = async () => {
    const response = await Axios("http://localhost:8000/recommend_movie?movie=" + params);
    // console.log('response',response)
    var data = response.data
    console.log(data)
    fetchRecommended(data['data'])

  };
  const fetchRecommended = async (data) => {

    console.log('fdata',data['data'])
    for(var i in data){
        console.log(i)
    }
    // console.log('sdata', data['exact match'])
    var exact_match_f = data['exact match']['title']
    // console.log('edata',exact_match_f)
    setExact([exact_match_f])
    if( data['recommended_match']['By Name'] != null){
        setName(convert_react_child(data['recommended_match']['By Name'],'title'))
    }
    if( data['recommended_match']['By Genre'] != null){
    setGenre(convert_react_child(data['recommended_match']['By Genre'],'title'))
    }
    if( data['recommended_match']['By Cast'] != null){
    setCast(convert_react_child(data['recommended_match']['By Cast'],'title'))
    }
    if( data['recommended_match']['final_show_to_user'] != null){
    setFinal(convert_react_child(data['recommended_match']['final_show_to_user'],'title'))
    }
    // console.log("length= "+scraps)
  };
  const convert_react_child = (data, key) =>{
    var ans = []
    var curr = 0
    // console.log('ccccccccc', data)
    for(var i in data){
        // console.log('ccccccccc', data[i][key])
      ans.push(data[i][key],);
    }
    return ans
  }


  return (
    <div className="App">
      <div className="show">
        
        {exact_match.length > 0  && <ExpandableList data={exact_match} header={"Exact Movies"}/>}
        
        {recommend_by_name.length > 0 && <ExpandableList data={recommend_by_name} header={"Recommended By Name"}/>}

        {recommend_final.length > 0 &&  <ExpandableList data={recommend_final} header ={"Final Recommendation"}/>}

        {recommend_by_genre.length>0  && <ExpandableList data={recommend_by_genre} header={"recommended By Genre"}/>}

        {recommend_by_cast.length > 0 && <ExpandableList data={recommend_by_cast} header={ "Recommended By Cast"}/>}

      </div>
    </div>
  );
}

export default Recommend;