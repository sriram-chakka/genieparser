expected_output = {
        "address-family":{
           "ipv4":{
              "areas":{
                 "0.0.0.0":{
                    "interfaces":{
                       "GigabitEthernet2":{
                          "neighbors":{
                             "10.16.2.2":{
                                "neighbor_router_id":"10.16.2.2",
                                "interface":"GigabitEthernet2",
                                "address":"10.1.2.2",
                                "interface_id":"unknown",
                                "priority":1,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":0,
                                   "last_retrans_scan_length":0,
                                   "last_retrans_max_scan_length":0,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"10.1.2.1",
                                "bdr_ip_addr":"10.1.2.2",
                                "hello_options":"0x2",
                                "dbd_options":"0x42",
                                "dead_timer":"00:00:33",
                                "uptime":"08:04:20",
                                "index":"1/2/2,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       },
                       "GigabitEthernet1":{
                          "neighbors":{
                             "10.64.4.4":{
                                "neighbor_router_id":"10.64.4.4",
                                "interface":"GigabitEthernet1",
                                "address":"10.1.4.4",
                                "priority":1,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":1,
                                   "last_retrans_scan_length":0,
                                   "last_retrans_max_scan_length":1,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"10.1.4.4",
                                "bdr_ip_addr":"10.1.4.1",
                                "dead_timer":"00:00:35",
                                "uptime":"1d01h",
                                "index":"1/1/1,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       }
                    }
                 },
                 "0.0.0.1":{
                    "sham_links":{
                       "OSPF_SL1":{
                          "neighbors":{
                             "10.151.22.22":{
                                "neighbor_router_id":"10.151.22.22",
                                "interface":"OSPF_SL1",
                                "address":"10.151.22.22",
                                "priority":0,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":2,
                                   "last_retrans_scan_length":1,
                                   "last_retrans_max_scan_length":1,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"0.0.0.0",
                                "bdr_ip_addr":"0.0.0.0",
                                "hello_options":"0x2",
                                "dbd_options":"0x42",
                                "dead_timer":"00:00:35",
                                "uptime":"07:41:59",
                                "index":"1/2/2,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       }
                    },
                    "interfaces":{
                       "GigabitEthernet3":{
                          "neighbors":{
                             "10.115.55.55":{
                                "neighbor_router_id":"10.115.55.55",
                                "interface":"GigabitEthernet3",
                                "address":"10.186.5.5",
                                "priority":1,
                                "state":"full",
                                "statistics":{
                                   "nbr_event_count":6,
                                   "nbr_retrans_qlen":0,
                                   "total_retransmission":6,
                                   "last_retrans_scan_length":1,
                                   "last_retrans_max_scan_length":6,
                                   "last_retrans_scan_time_msec":0,
                                   "last_retrans_max_scan_time_msec":0
                                },
                                "dr_ip_addr":"10.186.5.1",
                                "bdr_ip_addr":"10.186.5.5",
                                "dead_timer":"00:00:34",
                                "uptime":"15:47:14",
                                "index":"1/1/1,",
                                "first":"0x0(0)/0x0(0)/0x0(0)",
                                "next":"0x0(0)/0x0(0)/0x0(0)"
                             }
                          }
                       }
                    }
                 }
              }
           }
        }
    }