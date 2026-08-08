#!/usr/bin/env python3
"""
Output Formatter - Format and display results
"""

from typing import Dict, Any
import csv
import io


class OutputFormatter:
    """Format results for display"""
    
    def print_table(self, data: Dict[str, Any]):
        """Print results as a formatted table"""
        if not data:
            print("No data to display")
            return
        
        print("\n" + "=" * 60)
        print(f"📊 IP Analysis Results")
        print("=" * 60)
        
        # Display basic info
        print(f"\n🔍 IP: {data.get('ip', 'N/A')}")
        print(f"📅 Timestamp: {data.get('timestamp', 'N/A')}")
        
        # Display analysis sections
        analysis = data.get('analysis', {})
        if 'geolocation' in analysis:
            self._print_geo(analysis['geolocation'])
        if 'network' in analysis:
            self._print_network(analysis['network'])
        if 'dns' in analysis:
            self._print_dns(analysis['dns'])
        if 'whois' in analysis:
            self._print_whois(analysis['whois'])
        if 'threat' in analysis:
            self._print_threat(analysis['threat'])
        
        print("\n" + "=" * 60)
    
    def _print_geo(self, geo: Dict):
        """Print geolocation data"""
        print("\n📍 Geolocation:")
        if geo.get('success'):
            print(f"  Country: {geo.get('country', 'N/A')}")
            print(f"  City: {geo.get('city', 'N/A')}")
            print(f"  ISP: {geo.get('isp', 'N/A')}")
            print(f"  Coordinates: {geo.get('latitude', 'N/A')}, {geo.get('longitude', 'N/A')}")
        else:
            print(f"  ❌ Error: {geo.get('error', 'Unknown error')}")
    
    def _print_network(self, network: Dict):
        """Print network data"""
        print("\n🌐 Network:")
        print(f"  Class: {network.get('class', 'N/A')}")
        print(f"  Type: {network.get('type', 'N/A')}")
        print(f"  Binary: {network.get('binary', 'N/A')}")
    
    def _print_dns(self, dns: Dict):
        """Print DNS data"""
        print("\n📡 DNS:")
        reverse_dns = dns.get('reverse_dns')
        if reverse_dns:
            print(f"  Reverse DNS: {reverse_dns}")
        else:
            print("  Reverse DNS: No record found")
    
    def _print_whois(self, whois: Dict):
        """Print WHOIS data"""
        print("\n📋 WHOIS:")
        if whois.get('success'):
            registrar = whois.get('registrar', 'N/A')
            print(f"  Registrar: {registrar}")
            print(f"  Organization: {whois.get('org', 'N/A')}")
            print(f"  Country: {whois.get('country', 'N/A')}")
        else:
            print(f"  ❌ Error: {whois.get('error', 'Unknown error')}")
    
    def _print_threat(self, threat: Dict):
        """Print threat intelligence data"""
        print("\n🛡️ Threat Intelligence:")
        print(f"  Threat Score: {threat.get('threat_score', 0)}")
        print(f"  Total Reports: {threat.get('total_reports', 0)}")
        print(f"  Malicious: {'⚠️ YES' if threat.get('malicious') else '✅ NO'}")
    
    def to_csv(self, data: Dict[str, Any]) -> str:
        """Convert results to CSV format"""
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Category', 'Field', 'Value'])
        
        # Flatten the data
        for category, values in data.get('analysis', {}).items():
            if isinstance(values, dict):
                for key, value in values.items():
                    if key not in ['error', 'success']:
                        writer.writerow([category, key, str(value)])
        
        return output.getvalue()
