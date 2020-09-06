import React from 'react'


export default ({ portfolioLinks }) => {
    return (
        <section className="bg-light page-section" id="portfolio">
        <div className="container">
          <div className="row">
            <div className="col-lg-12 text-center">
              <h2 className="section-heading text-uppercase">Skills</h2>
              <h3 className="section-subheading text-muted"> In modern day, skills are more precious than Diamonds.</h3>
            </div>
          </div>
          <div className="row">
            {
                portfolioLinks && portfolioLinks.map(({ title, caption,image }, index) => 
                    <div className="col-md-3 col-sm-6 portfolio-item">
                        <div className="portfolio-caption">

              
                            <img className="rounded-circle img-fluid" src={image} alt="portfolio_img"/>
                            <h5>{ title }</h5>
          
                        </div>
                    

                     </div>
                )
            }
          </div>
        </div>
      </section>
    )
}