

def html_maker():
    

#416      updated_airbnb_map    
    
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <link href="http://fonts.googleapis.com/css?family=Lato:400,700,900" rel="stylesheet" type="text/css">
        <link href="{}/airbnb_app/static/ia_copy_tooltip.css" rel="stylesheet" type="text/css">""".format(BASE_DIR) + """
        </head>
        <div id="listingHover" class="pinned" style="left: 50px; visibility: visible; top: auto; bottom: 2px;">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" id="closeHover" style="visibility: visible;"><span aria-hidden="true">×</span></button>
            <div class="hostDetailsContainer">
                <p><a id="listingHost" target="_blank" href="http://www.airbnb.com/users/show/{}">""".format(host_id) + """{}</a>""".format(host_name) + """ ({}) </p>""".format(host_location) + """ 
                <!-- want to say if have liscenese then show the number if not then say no liscnese illegal etc with django template can use if logic block -->
                <p id="listingHostLicense"><span id="listingHostLicense">Hosting since: {}</span>""".format(host_since) + """</p>
                <p id="listingHostLicense"><span id="listingHostLicense">{}</span>""".format(license) + """ No License </p>
                <p id="listingHostCountContainer">(<span id="listingHostListingCount">{}</span>""".format(host_total_listings_count) + """ other listings locally)</p>
            </div>
            <div class="listingDetailsContainer">
                <p id="listingIDContainer"><a id="listingID" target="_blank" href={}>""".format(listing_url) + """ {}</a>""".format(listing_id) + """</p>
                <p id="listingNameContainer"><a id="listingName" target="_blank" href={}>""".format(listing_url) + """{}</a>""".format(listing_name) + """</p>
                <p id="listingNeighbourhood">{}</p>""".format(neighbourhood_cleansed) + """
                <p id="listingNeighbourhoodDistDuomo">{} meters to the Duomo</p>""".format(dist_duomo) + """
                <p id="listingRoomType">{} ({} bedrooms, accommodates {})</p>""".format(room_type, bedrooms, accommodates) + """
            </div>
            <div id="listingPriceSection" class="listingSection">
                <p class="listingSectionHeadlineContainer">
                    <span class="listingSectionHeadline"><span class="dollarSign">€</span><span id="listingEstimatedIncomePerYear">{}</span>""".format(rounded_revenue_ltm) + """</span><span id="listingPriceLabel" class="listingSectionHeadlineLabel"> income/year (est.)</span>
                </p>
                <p <span class="listingSectionSubhead"><span class="dollarSign">€</span><span id="listingEstimatedIncomePerMonth">{}</span>""".format(monthly_rounded_revenue_ltm) + """</span><span id="listingPriceLabel" class="listingSectionSubhead"> income/month (est.)</span> </p>
                <p class="listingSectionSubhead"><span class="dollarSign">€</span><span id="listingPrice">{}</span>""".format(price) + """/night</p>
            </div>
            <div id="listingReviewsSection" class="listingSection">
                <p class="listingSectionHeadlineContainer">
                    <span class="listingSectionSubhead"><span id="listingEstimatedNightsPerYear" class="listingSectionHeadline">{}</span>""".format(days_rented_ltm) + """<span class="listingSectionHeadlineLabel"> nights/year (est.)</span></span>
                </p>
                <!-- <p class="listingSectionSubhead"><span id="listingEstimatedOccupancyRate">23.4</span>% occupancy rate (est.)</p> -->
                <p class="listingSectionSubhead"><span id="listingReviewPerMonth">{}</span>""".format(reviews_per_month) + """ reviews/month</p>
                <!-- <p class="listingSectionSubhead"><span id="listingNumberOfReviews">5</span><span id="listingReviewsLabel"> reviews</span></p> -->
                <!-- <p class="listingSectionSubhead">last: <span id="listingLastReview">31/10/2021</span></p> -->
            </div>
            <div id="listingCensusSection" class= "listingSection">
            </div>
            <p class="listingSection">click listing on map to "pin" details</p>
            <p class="listingSection">the style for this popup was created by <a href="http://insideairbnb.com/">Inside Airbnb</a></p>
        </div>
        </html>
            """  


#278 original_airbnb_map 

html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <link href="http://fonts.googleapis.com/css?family=Lato:400,700,900" rel="stylesheet" type="text/css">
        <link href="{}/airbnb_app/static/ia_copy_tooltip.css" rel="stylesheet" type="text/css">""".format(BASE_DIR) + """
        </head>
        <div id="listingHover" class="pinned" style="left: 50px; visibility: visible; top: auto; bottom: 2px;">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" id="closeHover" style="visibility: visible;"><span aria-hidden="true">×</span></button>
            <div class="hostDetailsContainer">
                <p><a id="listingHost" target="_blank" href="http://www.airbnb.com/users/show/{}">""".format(host_id) + """{}</a>""".format(host_name) + """ ({}) </p>""".format(host_location) + """ 
                <!-- want to say if have liscenese then show the number if not then say no liscnese illegal etc with django template can use if logic block -->
                <p id="listingHostLicense"><span id="listingHostLicense">Hosting since: {}</span>""".format(host_since) + """</p>
                <p id="listingHostLicense"><span id="listingHostLicense">{}</span>""".format(license) + """ No License </p>
                <p id="listingHostCountContainer">(<span id="listingHostListingCount">{}</span>""".format(host_total_listings_count) + """ other listings locally)</p>
            </div>
            <div class="listingDetailsContainer">
                <p id="listingIDContainer"><a id="listingID" target="_blank" href={}>""".format(listing_url) + """ {}</a>""".format(listing_id) + """</p>
                <p id="listingNameContainer"><a id="listingName" target="_blank" href={}>""".format(listing_url) + """{}</a>""".format(listing_name) + """</p>
                <p id="listingNeighbourhood">{}</p>""".format(neighbourhood_cleansed) + """
                <p id="listingNeighbourhoodDistDuomo">{} meters to the Duomo</p>""".format(dist_duomo) + """
                <p id="listingRoomType">{} ({} bedrooms, accommodates {})</p>""".format(room_type, bedrooms, accommodates) + """
            </div>
            <div id="listingPriceSection" class="listingSection">
                <p class="listingSectionHeadlineContainer">
                    <span class="listingSectionHeadline"><span class="dollarSign">€</span><span id="listingEstimatedIncomePerYear">{}</span>""".format(rounded_revenue_ltm) + """</span><span id="listingPriceLabel" class="listingSectionHeadlineLabel"> income/year (est.)</span>
                </p>
                <p <span class="listingSectionSubhead"><span class="dollarSign">€</span><span id="listingEstimatedIncomePerMonth">{}</span>""".format(monthly_rounded_revenue_ltm) + """</span><span id="listingPriceLabel" class="listingSectionSubhead"> income/month (est.)</span> </p>
                <p class="listingSectionSubhead"><span class="dollarSign">€</span><span id="listingPrice">{}</span>""".format(price) + """/night</p>
            </div>
            <div id="listingReviewsSection" class="listingSection">
                <p class="listingSectionHeadlineContainer">
                    <span class="listingSectionSubhead"><span id="listingEstimatedNightsPerYear" class="listingSectionHeadline">{}</span>""".format(days_rented_ltm) + """<span class="listingSectionHeadlineLabel"> nights/year (est.)</span></span>
                </p>
                <!-- <p class="listingSectionSubhead"><span id="listingEstimatedOccupancyRate">23.4</span>% occupancy rate (est.)</p> -->
                <p class="listingSectionSubhead"><span id="listingReviewPerMonth">{}</span>""".format(reviews_per_month) + """ reviews/month</p>
                <!-- <p class="listingSectionSubhead"><span id="listingNumberOfReviews">5</span><span id="listingReviewsLabel"> reviews</span></p> -->
                <!-- <p class="listingSectionSubhead">last: <span id="listingLastReview">31/10/2021</span></p> -->
            </div>
            <div id="listingCensusSection" class= "listingSection">
            </div>
            <p class="listingSection">click listing on map to "pin" details</p>
            <p class="listingSection">the style for this popup was created by <a href="http://insideairbnb.com/">Inside Airbnb</a></p>

        </div>
        </html>
            """  



#485 updated_airbnb_map 

html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <link href="http://fonts.googleapis.com/css?family=Lato:400,700,900" rel="stylesheet" type="text/css">
        <link href="{}/airbnb_app/static/ia_copy_tooltip.css" rel="stylesheet" type="text/css">""".format(BASE_DIR) + """
        </head>
        <div id="listingHover" class="pinned" style="left: 50px; visibility: visible; top: auto; bottom: 2px;">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close" id="closeHover" style="visibility: visible;"><span aria-hidden="true">×</span></button>
            <div class="hostDetailsContainer">
                <p><a id="listingHost" target="_blank" href="http://www.airbnb.com/users/show/{}">""".format(host_id) + """{}</a>""".format(host_name) + """ ({}) </p>""".format(host_location) + """ 
                <!-- want to say if have liscenese then show the number if not then say no liscnese illegal etc with django template can use if logic block -->
                <p id="listingHostLicense"><span id="listingHostLicense">Hosting since: {}</span>""".format(host_since) + """</p>
                <p id="listingHostLicense"><span id="listingHostLicense">{}</span>""".format(license) + """ No License </p>
                <p id="listingHostCountContainer">(<span id="listingHostListingCount">{}</span>""".format(host_total_listings_count) + """ other listings locally)</p>
            </div>
            <div class="listingDetailsContainer">
                <p id="listingIDContainer"><a id="listingID" target="_blank" href={}>""".format(listing_url) + """ {}</a>""".format(listing_id) + """</p>
                <p id="listingNameContainer"><a id="listingName" target="_blank" href={}>""".format(listing_url) + """{}</a>""".format(listing_name) + """</p>
                <p id="listingNeighbourhood">{}</p>""".format(neighbourhood_cleansed) + """
                <p id="listingNeighbourhoodDistDuomo">{} meters to the Duomo</p>""".format(dist_duomo) + """
                <p id="listingRoomType">{} ({} bedrooms, accommodates {})</p>""".format(room_type, bedrooms, accommodates) + """
            </div>
            <div id="listingPriceSection" class="listingSection">
                <p class="listingSectionHeadlineContainer">
                    <span class="listingSectionHeadline"><span class="dollarSign">€</span><span id="listingEstimatedIncomePerYear">{}</span>""".format(rounded_revenue_ltm) + """</span><span id="listingPriceLabel" class="listingSectionHeadlineLabel"> income/year (est.)</span>
                </p>
                <p <span class="listingSectionSubhead"><span class="dollarSign">€</span><span id="listingEstimatedIncomePerMonth">{}</span>""".format(monthly_rounded_revenue_ltm) + """</span><span id="listingPriceLabel" class="listingSectionSubhead"> income/month (est.)</span> </p>
                <p class="listingSectionSubhead"><span class="dollarSign">€</span><span id="listingPrice">{}</span>""".format(price) + """/night</p>
            </div>
            <div id="listingReviewsSection" class="listingSection">
                <p class="listingSectionHeadlineContainer">
                    <span class="listingSectionSubhead"><span id="listingEstimatedNightsPerYear" class="listingSectionHeadline">{}</span>""".format(days_rented_ltm) + """<span class="listingSectionHeadlineLabel"> nights/year (est.)</span></span>
                </p>
                <!-- <p class="listingSectionSubhead"><span id="listingEstimatedOccupancyRate">23.4</span>% occupancy rate (est.)</p> -->
                <p class="listingSectionSubhead"><span id="listingReviewPerMonth">{}</span>""".format(reviews_per_month) + """ reviews/month</p>
                <!-- <p class="listingSectionSubhead"><span id="listingNumberOfReviews">5</span><span id="listingReviewsLabel"> reviews</span></p> -->
                <!-- <p class="listingSectionSubhead">last: <span id="listingLastReview">31/10/2021</span></p> -->
            </div>
            <div id="listingCensusSection" class= "listingSection">
            </div>
            <p class="listingSection">click listing on map to "pin" details</p>
        </div>
        </html>
            """  
