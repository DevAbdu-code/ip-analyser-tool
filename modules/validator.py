#!/usr/bin/env python3
"""
IP Validator Module - Validates and normalizes IP addresses
"""

import ipaddress
import re
from typing import Union, Optional


class IPValidator:
    """Validate and normalize IP addresses"""
    
    def __init__(self):
        self.ipv4_pattern = re.compile(
            r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
            r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        )
    
    def validate(self, ip: str) -> bool:
        """
        Validate if the string is a valid IPv4 address
        
        Args:
            ip: IP address string
            
        Returns:
            bool: True if valid, False otherwise
        """
        if not ip or not isinstance(ip, str):
            return False
        
        # Check format
        if not self.ipv4_pattern.match(ip):
            return False
        
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False
    
    def normalize(self, ip: str) -> Optional[str]:
        """Normalize IP address to standard format"""
        try:
            return str(ipaddress.IPv4Address(ip))
        except Exception:
            return None
    
    def validate_list(self, ips: list) -> list:
        """Validate a list of IP addresses"""
        return [ip for ip in ips if self.validate(ip)]
