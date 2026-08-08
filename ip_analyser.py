#!/usr/bin/env python3
"""
IP Intelligence Tool v2.0
A comprehensive IP address analysis and intelligence gathering tool

Author: Abdu (DevAbdu-code)
License: CC BY-ND 4.0
"""

import argparse
import json
import sys
from typing import Dict, Any, Optional
import socket
import ipaddress
import requests
from datetime import datetime

# Import custom modules
from modules.validator import IPValidator
from modules.geolocation import GeolocationService
from modules.dns_lookup import DNSResolver
from modules.whois_lookup import WHOISService
from modules.network_info import NetworkAnalyzer
from modules.security_check import ThreatIntel
from utils.formatter import OutputFormatter


class IPIntelligenceTool:
    """Main class for the IP Intelligence Tool"""

    def __init__(self, timeout: int = 10, use_cache: bool = True):
        """Initialize the tool with configuration"""
        self.timeout = timeout
        self.use_cache = use_cache
        self.results = {}
        self.formatter = OutputFormatter()
        
        # Initialize services
        self.validator = IPValidator()
        self.geo_service = GeolocationService(timeout=timeout)
        self.dns_resolver = DNSResolver()
        self.whois_service = WHOISService()
        self.network_analyzer = NetworkAnalyzer()
        self.threat_intel = ThreatIntel()

    def analyze_ip(self, ip_address: str, modules: Optional[list] = None) -> Dict[str, Any]:
        """
        Perform comprehensive analysis on an IP address
        
        Args:
            ip_address: The IP address to analyze
            modules: List of modules to run (None = all)
        
        Returns:
            Dict containing all analysis results
        """
        if not self.validator.validate(ip_address):
            raise ValueError(f"Invalid IP address: {ip_address}")
        
        results = {
            "ip": ip_address,
            "timestamp": datetime.now().isoformat(),
            "analysis": {}
        }
        
        # Run all modules or specified ones
        modules_to_run = modules or ['geo', 'dns', 'whois', 'network', 'threat']
        
        if 'geo' in modules_to_run:
            results['analysis']['geolocation'] = self._get_geolocation(ip_address)
        
        if 'dns' in modules_to_run:
            results['analysis']['dns'] = self._get_dns_info(ip_address)
        
        if 'whois' in modules_to_run:
            results['analysis']['whois'] = self._get_whois(ip_address)
        
        if 'network' in modules_to_run:
            results['analysis']['network'] = self._get_network_info(ip_address)
        
        if 'threat' in modules_to_run:
            results['analysis']['threat'] = self._get_threat_info(ip_address)
        
        self.results = results
        return results

    def _get_geolocation(self, ip: str) -> Dict[str, Any]:
        """Get geolocation information"""
        try:
            return self.geo_service.get_info(ip)
        except Exception as e:
            return {"error": str(e)}

    def _get_dns_info(self, ip: str) -> Dict[str, Any]:
        """Get DNS information"""
        try:
            return self.dns_resolver.resolve(ip)
        except Exception as e:
            return {"error": str(e)}

    def _get_whois(self, ip: str) -> Dict[str, Any]:
        """Get WHOIS information"""
        try:
            return self.whois_service.query(ip)
        except Exception as e:
            return {"error": str(e)}

    def _get_network_info(self, ip: str) -> Dict[str, Any]:
        """Get network analysis"""
        try:
            return self.network_analyzer.analyze(ip)
        except Exception as e:
            return {"error": str(e)}

    def _get_threat_info(self, ip: str) -> Dict[str, Any]:
        """Get threat intelligence"""
        try:
            return self.threat_intel.check(ip)
        except Exception as e:
            return {"error": str(e)}

    def display_results(self, results: Dict[str, Any], format: str = 'table'):
        """Display results in various formats"""
        if format == 'json':
            print(json.dumps(results, indent=2))
        elif format == 'csv':
            print(self.formatter.to_csv(results))
        else:
            self.formatter.print_table(results)

    def export_results(self, results: Dict[str, Any], filename: str, format: str = 'json'):
        """Export results to file"""
        if format == 'json':
            with open(filename, 'w') as f:
                json.dump(results, f, indent=2)
        elif format == 'csv':
            with open(filename, 'w') as f:
                f.write(self.formatter.to_csv(results))
        else:
            self.formatter.print_table(results)
        print(f"✅ Results exported to {filename}")


def main():
    """Command-line interface entry point"""
    parser = argparse.ArgumentParser(
        description='IP Intelligence Tool - Comprehensive IP analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ip_analyser.py 8.8.8.8
  ip_analyser.py 8.8.8.8 --format json
  ip_analyser.py 8.8.8.8 --output report.json
  ip_analyser.py 8.8.8.8 --modules geo,dns
        """
    )
    
    parser.add_argument('ip', help='IP address to analyze')
    parser.add_argument(
        '--format', '-f',
        choices=['table', 'json', 'csv'],
        default='table',
        help='Output format (default: table)'
    )
    parser.add_argument(
        '--output', '-o',
        help='Export results to file'
    )
    parser.add_argument(
        '--modules', '-m',
        help='Comma-separated modules: geo,dns,whois,network,threat'
    )
    parser.add_argument(
        '--timeout', '-t',
        type=int,
        default=10,
        help='Timeout in seconds (default: 10)'
    )
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help='Disable cache'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    
    args = parser.parse_args()
    
    try:
        # Parse modules
        modules = args.modules.split(',') if args.modules else None
        
        # Initialize tool
        tool = IPIntelligenceTool(
            timeout=args.timeout,
            use_cache=not args.no_cache
        )
        
        if args.verbose:
            print(f" Analyzing IP: {args.ip}")
            print("⏳ Please wait...")
        
        # Run analysis
        results = tool.analyze_ip(args.ip, modules)
        
        # Display results
        if args.output:
            format_type = args.format if args.format != 'table' else 'json'
            tool.export_results(results, args.output, format_type)
        else:
            tool.display_results(results, args.format)
            
    except ValueError as e:
        print(f" Error: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n  Interrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f" Unexpected error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
