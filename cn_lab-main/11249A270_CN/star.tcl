set ns [new Simulator]
set tf [open star.tr w]
$ns trace-all $tf
set nf [open star.nam w]
$ns namtrace-all $nf
set n0 [$ns node]

set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
$ns duplex-link $n0 $n1 1mb 10Ms DropTail
$ns duplex-link $n0 $n2 1mb 10Ms DropTail
$ns duplex-link $n0 $n3 1mb 10Ms DropTail
$ns duplex-link $n0 $n4 1mb 10Ms DropTail

set udp[new Agent/UDP]
$ns attach-Agent $n1$udp
set null [new agent/Null]
$ns attach-Agent $n4 $null
$ns connect$udp $null
set cbr[new Application/Traffic/CBR]
$cbr attach-agent$n1$udp
$cbr packetSize_500
$cbr interval_0.05
proc finish{}{
global ns tf nf
$ns flush-trace
close.tf
close.nf
exce nam star.nam & 
exit 0()
}
$ns at 1.0"$cbr start"
$ns at 5.0"finish"
$ns run
