#!/usr/bin/env python3
"""
Geolocation Module - Get IP geolocation information
"""

import requests
from typing import Dict, Any, Optional


class GeolocationService:
    """Service to get geolocation information for IP addresses"""
    
    def __init__(self, timeout: int = 10):
        self.timeout = timeout
        self.api_url = "http://ip-api.com/json/"
    
    def get_info(self, ip: str) -> Dict[str, Any]:
        """
        Get geolocation information for an IP
        
        Args:
            ip: IP address
            
        Returns:
            Dict with geolocation data
        """
        try:
            response = requests.get(
                f"{self.api_url}{ip}",
                timeout=self.timeout,
                params={"fields": "status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,query"}
            )
            response.raise_for_status()
            data = response.json()
            
            if data.get('status') == 'fail':
                return {
                    "error": data.get('message', 'Unknown error'),
                    "success": False
                }
            
            return {
                "success": True,
                "ip": data.get('query'),
                "country": data.get('country'),
                "country_code": data.get('countryCode'),
                "region": data.get('regionName'),
                "city": data.get('city'),
                "zip": data.get('zip'),
                "latitude": data.get('lat'),
                "longitude": data.get('lon'),
                "timezone": data.get('timezone'),
                "isp": data.get('isp'),
                "organization": data.get('org'),
                "asn": data.get('as'),
                "asn_name": data.get('asname')
            }
        except requests.exceptions.RequestException as e:
            return {"error": f"Request failed: {str(e)}", "success": False}
        except Exception as e:
            return {"error": f"Unexpected error: {str(e)}", "success": False}
