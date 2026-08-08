#!/usr/bin/env python3
"""
Network Info Module - Analyze IP network properties
"""

import ipaddress
from typing import Dict, Any


class NetworkAnalyzer:
    """Analyze network properties of IP addresses"""
    
    def analyze(self, ip: str) -> Dict[str, Any]:
        """
        Analyze network properties
        
        Args:
            ip: IP address
            
        Returns:
            Dict with network information
        """
        try:
            ip_obj = ipaddress.IPv4Address(ip)
            first_octet = int(str(ip_obj).split('.')[0])
            
            # Determine class
            ip_class, default_subnet = self.get_class_and_subnet(first_octet)
            
            # Determine type (public/private)
            ip_type = self.get_ip_type(ip_obj)
            
            return {
                "version": "IPv4",
                "class": ip_class,
                "default_subnet": default_subnet,
                "type": ip_type,
                "binary": self.to_binary(ip_obj),
                "hexadecimal": self.to_hex(ip_obj)
            }
        except Exception as e:
            return {"error": str(e)}
    
    def get_class_and_subnet(self, first_octet: int) -> tuple:
        """Determine IP class and default subnet"""
        if 1 <= first_octet <= 126:
            return "Class A", "/8"
        elif 128 <= first_octet <= 191:
            return "Class B", "/16"
        elif 192 <= first_octet <= 223:
            return "Class C", "/24"
        elif 224 <= first_octet <= 239:
            return "Class D (Multicast)", "N/A"
        elif 240 <= first_octet <= 255:
            return "Class E (Experimental)", "N/A"
        return "Invalid", "N/A"
    
    def get_ip_type(self, ip: ipaddress.IPv4Address) -> str:
        """Determine if IP is public or private"""
        if ip.is_private:
            return "Private"
        elif ip.is_multicast:
            return "Multicast"
        elif ip.is_loopback:
            return "Loopback"
        elif ip.is_link_local:
            return "Link Local"
        else:
            return "Public"
    
    def to_binary(self, ip: ipaddress.IPv4Address) -> str:
        """Convert IP to binary representation"""
        return '.'.join([format(int(octet), '08b') for octet in str(ip).split('.')])
    
    def to_hex(self, ip: ipaddress.IPv4Address) -> str:
        """Convert IP to hexadecimal representation"""
        return '.'.join([hex(int(octet))[2:].upper().zfill(2) for octet in str(ip).split('.')])
