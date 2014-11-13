from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    darkcoin=math.Object(
        PARENT=networks.nets['darkcoin'],
	SHARE_PERIOD=15, # seconds
	CHAIN_LENGTH=24*60*60//15, # shares
	REAL_CHAIN_LENGTH=24*60*60//15, # shares
	TARGET_LOOKBEHIND=200, # shares //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
	SPREAD=30, # blocks
	#IDENTIFIER='496247d46a00c115'.decode('hex'),
	#PREFIX='5685a273806675db'.decode('hex'),
	IDENTIFIER='ef05d164bbcd7ed1'.decode('hex'),
	PREFIX='3966e45ab1ed2db9'.decode('hex'),
        P2P_PORT=29968,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=7903,
	#BOOTSTRAP_ADDRS='p2phash.com:7902 asia02.poolhash.org:7902 asia01.poolhash.org:7902 157.56.161.11:7902 54.186.8.140:7902 62.141.39.175:7902 mightypool.net:7902 85.131.127.26:7902 213.229.88.102:7902 cryptohasher.net:7902 darkcoin.fr:7902'.split(' '),
        BOOTSTRAP_ADDRS='e-pool.net:29968 drk.altmine.net:8999 darkcoin.fr:8999 p2pool.crunchpool.com:8999 x11p2p.com:8999 happymining.de:8999 ca.p2pool.sk:8999 eu.p2pool.sk:8999 us.p2pool.sk:8999'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-drk',
	VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
