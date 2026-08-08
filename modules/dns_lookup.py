#!/usr/bin/env python3
"""
DNS Lookup Module - DNS resolution and query capabilities
"""

import socket
import dns.resolver
from typing import Dict, List, Any, Optional


class DNSResolver:
    """DNS resolution service"""
    
    def __init__(self):
        self.record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
    
    def resolve(self, ip: str) -> Dict[str, Any]:
        """
        Perform DNS lookups for an IP
        
        Args:
            ip: IP address
            
        Returns:
            Dict with DNS information
        """
        results = {
            "reverse_dns": self.get_reverse_dns(ip),
            "records": {}
        }
        
        # Try forward lookup for hostname
        hostname = self.get_hostname(ip)
        if hostname:
            for record_type in self.record_types:
                records = self.query_records(hostname, record_type)
                if records:
                    results['records'][record_type] = records
        
        return results
    
    def get_reverse_dns(self, ip: str) -> Optional[str]:
        """Get reverse DNS entry"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except socket.herror:
            return None
        except Exception:
            return None
    
    def get_hostname(self, ip: str) -> Optional[str]:
        """Get forward DNS entry"""
        try:
            return socket.gethostbyaddr(ip)[0]
        except Exception:
            return None
    
    def query_records(self, hostname: str, record_type: str) -> List[str]:
        """Query DNS records for a hostname"""
        try:
            resolver = dns.resolver.Resolver()
            answers = resolver.resolve(hostname, record_type)
            return [str(answer) for answer in answers]
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            return []
        except Exception:
            return []
