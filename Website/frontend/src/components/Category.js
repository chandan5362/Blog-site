import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const Category = (props) => {
    const [blogs, setBlogs] = useState([]);
    const [currentCategory, setCurrentCategory] = useState('');

    useEffect(() => {
        const category = props.match.params.id;
        setCurrentCategory(capitalizeFirstLetter(category));

        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        };

        const fetchData = async () => {
            try {
                const res = await axios.post(`${process.env.REACT_APP_API_URL}/api/Blog/category`, { category }, config);
                setBlogs(res.data);
            }
            catch (err) {

            }
        }

        fetchData();
    }, [props.match.params.id]);

    const capitalizeFirstLetter = (word) => {
        if (word)
            return word.charAt(0).toUpperCase() + word.slice(1);
        else
            return '';
    };

    const getCategoryBlogs = () => {
        let list = [];
        let result = [];

        blogs.map(blogPost => {
            return list.push(
                <div className="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
                    <div className="col p-4 d-flex flex-column position-static">
                        <strong className="d-inline-block mb-2 text-primary">{capitalizeFirstLetter(blogPost.category)}</strong>
                        <h3 className="mb-0">{blogPost.title}</h3>
                        <div className="mb-1 text-muted">{blogPost.month} {blogPost.day}</div>
                        <p className="card-text mb-auto">{blogPost.excerpt}</p>
                        <Link to={`/blog/${blogPost.slug}`} className="stretched-link">Continue reading</Link>
                    </div>
                    <div className="col-auto d-none d-lg-block">
                        <img width="200" height="250" src={blogPost.thumbnail} alt='' />
                    </div>
                    
                </div>
                
            );
        });

        for (let i = 0; i < list.length; i += 2) {
            result.push(
                <div key={i} className='row mb-2'>
                    <div className='col-md-6'>
                        {list[i]}
                    </div>
                    <div className='col-md-6'>
                        {list[i+1] ? list[i+1] : null}
                    </div>
                </div>
            );
        }

        return result;
    };

    return (
        <div className="container mt-3">
            
            <div className="p-3 mb-2 bg-light text-dark">
                <nav className="nav justify-content-between">
                    <h6><Link className="p-2 text-dark" to="/">Home</Link></h6>
                    <h6><Link className="p-2 text-muted" to="/category/Data Science">Data science</Link></h6>
                    <h6><Link className="p-2 text-muted" to="/category/Machine Learning">Machine learning</Link></h6>
                    <h6><Link className="p-2 text-muted" to="/category/Deep Learning">Deep Learning</Link></h6> 
                    <h6><Link className="p-2 text-muted" to="/category/Statistics">Statistics</Link></h6>
                    <h6><Link className="p-2 text-muted" to="/category/Data Structure and Algorithm">DS/Algo</Link></h6>
                    <h6><Link className="p-2 text-muted" to="/category/Projects">Projects</Link></h6>
                   
                </nav>
            </div>
            <h3 className='display-4'>{currentCategory}</h3>
            {getCategoryBlogs()}

            <p className="lead mb-5"><Link to='/Blog' className="font-weight-bold">Back to Blogs</Link></p>
        </div>
    );
};

export default Category;