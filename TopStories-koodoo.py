#!/usr/bin/env python
# coding: utf-8


#import the necessary packages

import requests as req
import xml.etree.ElementTree as ET
import traceback



def getData():
    """
    This function will return the data and the response code from the end point
    """
    try:
        response=req.get(api_endpoint)
        return response.text,response.status_code
    except Exception as err:
        print("Error : while getting the data from the endpoint")
        print(traceback.format_exc())


if __name__ == '__main__':
    # get the data from the endpoint
    api_endpoint="https://www.europarl.europa.eu/rss/doc/top-stories/en.xml"
    data,response=getData()
    
    # parse the response from endpoint
    if str(response) != req.codes.ok and data == '':
        print("Didn't receive a correct response from server please investigate, URL :",api_endpoint," response_code: ",response)
    else:
        try:
            root=ET.fromstring(data)
            print("Top stories below\n");print('*'*20)
            
            # since the Element item, which contains the "Top stories" is nested we need to traverse and loop it's parent channel
            for child in root:
                 print(root[0][0].text)
            
            count=1
            for child in root[0].iter('item'):
                print(count,') ',child[0].text)
                count=count+1;
            
        except Exception as err:
            print("Unable to parse the XML, please see error below")
            print(traceback.format_exc())



