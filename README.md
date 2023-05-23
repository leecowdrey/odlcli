![OpenDaylight CLI](odlcli-banner.png)


## PURPOSE
- OpenDaylight SDN Controller operational CLI interface

## NOTE
- Always refer to built-in help for latest options and instructions

## USAGE

```
$ odlcli [cmd]
```

or

```
$ odlcli
odlcli> [cmd]
odlcli> [cmd]
odlcli> [cmd]
odlcli> <CTRL>D
$
```

## DESCRIPTION
- odlcli  is  a  shell program for OpenDaylight/Lumina SDN Controller (SDNc) that provides Service Provider Network Operation teams a CLI orientated mechanism to perform common administrative tasks directly from a console prompt or other CLI tools/scripts to manage the operational aspects of the SDN Controller, without requiring knowledge of RESTCONF/NETCONF, installation/use of desktop orientated REST tools or NETCONF shells.

### OPTIONS
- odlcli requires commands and parameters to be supplied which can be supplied via STDIN; these can include:

#### AAA
       • Usage: aaa [key] [action] [options] Commands:
            domains add        <<domain-name>>
                               [--description <<text>>]
                               [--enable]
            domains disable    <<domain-name>>
            domains enable     <<domain-name>>
            doamins list
            domains delete     <<domain-name>>

            roles add          <<role-name>>
                               [--domain <<domain-name>>]
            roles list         [--domain <<domain-name>>]
            roles delete       <<role-name>>
                               [--domain <<domain-name>>]

            users add          <<username>>
                               [--domain <<domain-name>>]
                               [--description <<text>>]
                               [--enable]
                               [--email <<text>>]
                               [--password <<text>>]
            users delete       <<username>>
                               [--domain <<domain-name>>]
            users list         [--domain <<domain-name>>]
            users disable      <<username>>
                               [--domain <<domain-name>>]
            users enable       <<username>>
                               [--domain <<domain-name>>]
            users password     <<username>>"
                               --password <<text>>"
                               [--domain <<domain-name>>]

            policies add       <<url-resource>>
                               <<role-name>>
                               [--index <<index-value>> ]
                               [--get] [--post] [--put] [--patch] [--delete]
                               [--insert] [--append] [--line <<line-number>>]
                               [--domain <<domain-name>>]
            policies list      [--role <<role-name>>]
                               [--domain <<domain-name>>]
            policies delete    <<url-resourcee>>
                               [--role <<role-name>>]
                               [--domain <<domain-name>>]

          Attention
          - when <<domain-name>> is not supplied, domain will default to sdn
          - the default domain sdn can not be deleted, nor can the default user admin (on domain sdn)
          - insert/append new policies will be inserted before or appended after the supplied <<line-number>> - default is append
          - if no <<line-number>> supplied, append will be after exsting last policy and insert will be before last policy
          - URL resources should include all appropriate wildcards, i.e. /restconf/** , /rests/data/network-topology:network-topology/topology=topology-netconf/**

         Warning:
          - ALL deletes will automatically propagate where appropriate i.e. deleting a domain will also delete associated users and roles etc.; deleting a role will also delete associated policies

#### ABOUT
       • about - Copyright/version and contact information
#### CONFIGURE
       • configure - completely reconfigure environment 
#### DELETE
       • delete [parameter] - Remove [odlcli] environment parameters
            user/pass/protocol/host/port/prefix/timeout/maxtime can not be deleted
            <<name>>         Delete custom parameter
#### QUERY
       • query [method] [path] - RESTCONF generic query
            get '<<URL Path>>'         RESTCONF Get URL path, do not include /rests/data prefix i.e.
                                       GET '/network-topology:network-topology/topology=topology-netconf?content=nonconfig&fields=node(node-id)'
#### SITES (example for local customisation)
       • sites [cmd] - IETF L3VPN service/site retrieval
            list [svn-name]            List known sites vpn-name and nodes
#### STREAMS
       • streams [cmd] - RFC 8040 Events/Notifications
            bootstrap                  Used to intialize the RFC8040 Events/Notification streams upon SDNc startup (used primarily by Lumina SDN Controller, LSC)
                                       note: should not be generally used but will not cause harm and can be used
                                             to verify availability of capability
            list                       List currently available RFC8040 Events/Notification streams
                 [ --json-only       ] limit to JSON encoded streams
                 [ --xml-only        ] limit to XML encoded streams
            monitor <<stream>>         Interactively subscribe and display RFC8040 stream
                                       <<stream>> is stream location segment
                                       i.e. ietf-netconf-notifications:netconf-config-change
                 [ --json            ] JSON encoding, rather than default XML encoding
#### SET
       • set [parameter] [value] - Adjust [odlcli] environment parameters
            user      Set RESTCONF API username
            pass      Set RESTCONF API password
            protocol  Set RESTCONF API protocol
            host      Set RESTCONF API host
            port      Set RESTCONF API port number
            prefix    Set RESTCONF API path prefix
            timeout   Set RESTCONF API connection timeout (seconds)
            maxtime   Set RESTCONF API max wait timeout (seconds)
            <<name>>  Set custom parameter
            juser     Set Jolokia username
            jpass     Set Jolokia password
#### SHOW
       • show [parameter] | --all - View [odlcli] environment parameters and additional capabilities of the linked SDNc that are exposed via RESTCONF
            version     Show CLI version
            user        Show RESTCONF API username
            password    Show RESTCONF API password
            protocol    Show RESTCONF API protocol
            host        Show RESTCONF API host
            port        Show RESTCONF API port number
            prefix      Show RESTCONF API path prefix
            timeout     Show RESTCONF API connection timeout (seconds)
            maxtime     Show RESTCONF API max wait timeout (seconds)
            juser       Show Jolokia username
            jpass       Show Jolokia password
          Not included within --all
            capability  Show RESTCONF API offered capabilities
            <<name>>    Show customer parameter
#### STATS
       • stats [cmd] - Display various statistics of the SDNc (via Jolokia), including:
            runtime   List JVM runtime
            os        List Operating System
            memory    List JVM memory usage
            nodecount List Lumina Node Counter
            version   List SDNc component versions
#### NODES
       • nodes - Manage NETCONF nodes (network devices) connected to the SDNc
            aaa <<node-id>>                      Verify AAA access to specific node
               [ --name                        ] username to attempt access with, if not specified defualt will be used
               [ --password                    ] password to attempt access with, if not specififed default will be used
            export                               Extract mount commands for all known network devices/nodes
               [ --encrypt                     ] encrypt exported passwords
            list                                 List known nodes
            status                               List connection status of known nodes
            state <<node-id>> | --all            ONF control-construct operational state
                [  --yang-model <<model>>      ] YANG model, defaults to core-model-1-4
                [  --exclude <<node-id>>       ] Exclude specified node, repeat as necessary
                [  --extended                  ] Fetch LTPs and report status and size
                [  --timeout <<milliseconds>>  ] Maximum wait (milliseconds, default 60000)
            test <<node-id>> | --all             PING, SSH verify, NETCONF verify specified node or all known
                [  --timeout <<seconds>>       ] Maximum wait (seconds)
                [  --capabilities]             ] additional display reported NETCONF capabilities of the node(s)
            mount <<node-id>>                    Mount network device/node
                   --host <<ip>>                 node IP or FQDN
                   --username <<username>>       node NETCONF username
                   --password <<password>>       node NETCONF password
               [ --encrypted-password <<text>> ] use supplied encrypted password
               [ --port <<port number>>        ] node NETCONF port (default: 830)
               [ --cache <<dir>>               ] mount node schema cache directory
               [ --cschema                     ] node reconnect on changed schema
               [ --timeout <<milliseconds>>    ] node default request timeout
               [ --tcp-only                    ] node limited to TCP only
               [ --max-attempts <<attempts>>   ] maximum attempts of connecting to node, default 0/unlimited
               [ --concurrent <<rpc-limit>>    ] maximum of RPC to send before response received, default 0/unlimited
            ummount <<node-id>> | --all          Unmount network device/node or all
#### HELP
       • help - Additional help can be shown by adding the verb help after the command itself.
#### REFRESH
       • refresh - update SDNc RFC8040 capabilities, resource details etc.

#### OTHER
- When operating odlcli interactively, the command verb quit or key sequence <CTRL>D can be used to leave the CLI interface.

#### BUGS
- No known bugs.

#### SUPPORTED CLIENT PLATFORM
- RedHat Enterprise Linux (RHEL)/CentOS 7 and later
- Debian/Ubuntu 16.04 and later
- Windows Subsystem for Linux (WSL)

#### DEPENDENCIES
- `bash`
- `curl`
- `sed`
- `grep`
- `bc`
- `openssl`
- `jq`
- `sshpass`
- `openssh-client`
- `bash-completion`
- `libxml-xpath-perl`
- OpenDaylight Sodium or later

#### CONTROL
- Initial Author, Lee Cowdrey (lee@cowdrey.net)
- Initial Release, 1.1.0


#### PACKAGING/DISTRIBUTION
- Upstream-Name: odlcli
- Upstream-Contact: Lee Cowdrey <lee@cowdrey.net>
- Source: https://www.cowdrey.net/odlcli
- Formats: dpkg & rpm

#### INSTALLATION
- Debian/Ubuntu
```
$ sudo dpkg -i odlcli-1.1.0_amd64.deb
$ sudo dpkg -f install
```

- RedHat Enterprise Linux (RHEL)/CentOS
```
$ sudo rpm -ivH odlcli-1.0.0-2.noarch.rpm
```

##### Configuration Files
- `~/.odlcli`
- `/usr/lib/odlcli/config.template`

##### Core Files
- `/usr/bin/odlcli`
- `/usr/lib/odlcli/?`
- `/usr/lib/odlcli/aaa`
- `/usr/lib/odlcli/akka`
- `/usr/lib/odlcli/about`
- `/usr/lib/odlcli/banner.odlcli`
- `/usr/lib/odlcli/common`
- `/usr/lib/odlcli/config.template`
- `/usr/lib/odlcli/delete`
- `/usr/lib/odlcli/help`
- `/usr/lib/odlcli/nodes`
- `/usr/lib/odlcli/query`
- `/usr/lib/odlcli/set`
- `/usr/lib/odlcli/show`
- `/usr/lib/odlcli//sites`
- `/usr/lib/odlcli/stats`
- `/usr/lib/odlcli/streams`
- `/usr/share/man/man1/odlcli.1{.gz}`
- `/etc/bash_completion.d/odlcli.bash_completion`

#### COPYRIGHT TERMS

```
               Cowdrey Consulting UK Ltd <https://www.cowdrey.net/>
               OpenDaylight Project <https://www.opendaylight.org/>
                    License Eclipse Public License (EPL-1.0)
    <https://www.opendaylight.org/technical-community/ip-policy/licensing>
    <https://www.eclipse.org/legal/eplfaq.php#PARTIESEPL>
 
       This is free software; you are free to change and redistribute it.
            There is NO WARRANTY, to the extent permitted by law.
```
