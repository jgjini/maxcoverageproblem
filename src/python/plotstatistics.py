import matplotlib.pyplot as plt

file1= {1: [0.09028063533865525, 0.09028063533865525, 0.09028063533865525, 0.09028063533865525],
        2: [0.14509093901736483, 0.13085342770142375, 0.13085342770142375, 0.14509093901736483],
        3: [0.1856637313801333, 0.1856637313801333, 0.1856637313801333, 0.1856637313801333],
        4: [0.2217924450662497, 0.2240967821578471, 0.2217924450662497, 0.2240967821578471, 0.20582668093161058],
        5: [0.2414616080980989, 0.2602254958439635, 0.24425973170932433, 0.24977368117850382, 0.24771623734672044],
        6: [0.28186980495432473, 0.2752859846926179, 0.2882067319562176, 0.2810468274216114, 0.28343346226648014],
        7: [0.31092091185910625, 0.3128960579376183, 0.3069706197020821, 0.303267220804872, 0.31371903547033164, 0.31371903547033164],
        8: [0.3454036704797959, 0.3419471648423998, 0.33585713110032095, 0.34622664801250924, 0.3327298164760102],
        9: [0.3666364908238005, 0.36202781664060574, 0.3562669739116122, 0.3577483334704963],
        10: [0.38161468191918363, 0.3988972101061641, 0.38062710887992757, 0.39256028310427127, 0.39618138424821003],
        11: [0.4016953337173895, 0.4157682495267879, 0.4071269854332977, 0.3887745864537898, 0.3933832606369846],
        12: [0.43724796313060654, 0.41897786190437003, 0.4403752777549173, 0.42350423833429346, 0.4403752777549173],
        13: [0.44399637889885607, 0.45346062052505964, 0.4574932104353551, 0.4392231092091186, 0.43494362603900916, 0.4596329520204098, 0.4649823059830467, 0.4651469014895893, 0.4225989630483088],
        14: [0.48037198584478646, 0.4493457328614929, 0.47008476668586946, 0.46193728911200727],
        15: [0.5025923792280471, 0.4984774915644803, 0.45411900255123033, 0.4934573286149288],
        16: [0.5165006995309028, 0.5193811208953996, 0.5072010534112419, 0.5028392724878611, 0.5010287219158917],
        17: [0.5423421940581022, 0.4988066825775656, 0.5085178174635833, 0.5053082050860012],
        18: [0.5528763064768332, 0.5366636490823801, 0.5269525141963625, 0.5497489918525225],
        19: [0.5483499300469097, 0.5671961155460455, 0.558966340218912, 0.5607768907908814, 0.5537815817628179],
        20: [0.5495020985927084, 0.5632458233890215, 0.5721339807423257, 0.5639042054151922, 0.5877705538638796, 0.5610237840506954, 0.5846432392395687],
        21: [0.6066167393630154, 0.570981812196527, 0.6041478067648753, 0.5977285820097111],
        22: [0.5973993909966258, 0.5965764134639124, 0.5987161550489671, 0.5995391325816806, 0.6068636326228294, 0.5968233067237264, 0.5971524977368118],
        23: [0.6117192000658382, 0.6110608180396675, 0.6268619866677639, 0.6271911776808493, 0.6096617562340548, 0.6306476833182454, 0.628343346226648],
        24: [0.6254629248621513, 0.6305653855649741, 0.6197020821331578, 0.6207719529256851, 0.6164101720023043],
        25: [0.6439799193482018, 0.6371492058266809, 0.6443914081145584, 0.6480948070117686, 0.6582997284174142, 0.6357501440210682, 0.6565714755987162],
        26: [0.6481771047650399, 0.6806847173072175, 0.6819191836062876, 0.6481771047650399, 0.6604394700024689, 0.6498230598304666],
        27: [0.6958275039091433, 0.6906427454530492, 0.6672701835239898, 0.677639700436178],
        28: [0.6980495432474694, 0.7052917455353469, 0.6961566949222286, 0.7109702905110691, 0.7039749814830055, 0.686445560036211],
        29: [0.7288289029709489, 0.7209283186569007, 0.7266068636326228, 0.6865278577894823], 'file': 1}

file2= {1: [0.06863542513921041, 0.06863542513921041, 0.06863542513921041, 0.06863542513921041],
        2: [0.12019020208972032, 0.12019020208972032, 0.12019020208972032, 0.12019020208972032],
        3: [0.16085841206281673, 0.16185947569292372, 0.13389226052680975, 0.15610335981980855, 0.15610335981980855],
        4: [0.19777263342301196, 0.19777263342301196, 0.20252768566602014, 0.19345554651817556, 0.16648939498216855],
        5: [0.22567728211224425, 0.22861790652568353, 0.23268472752299318, 0.22461365200525557, 0.22467621848213726, 0.23512482012137897, 0.22861790652568353],
        6: [0.2659700932240506, 0.2663454920853407, 0.2663454920853407, 0.2591503472439467, 0.2538321967090033],
        7: [0.2866795970718889, 0.27009948069824186, 0.29612713508102356, 0.2805480823374836, 0.29719076518801224, 0.2938121754364012],
        8: [0.3174623036976788, 0.3273478070449853, 0.3174623036976788, 0.315022211099293, 0.3273478070449853],
        9: [0.3476819120315335, 0.3368579115310017, 0.3460551836326097, 0.3548144903960458, 0.33860977288368893],
        10: [0.376149659012701, 0.36926734655571547, 0.3785271851342051, 0.3643245948820622, 0.37677532378151785],
        11: [0.3657010573734593, 0.3932303072014015, 0.3982356253519364, 0.3828442720390415, 0.38434586748420196, 0.3856597634987174],
        12: [0.4021773133954827, 0.40230244634924606, 0.4005505849965588, 0.4082462616530063, 0.41856973033848466, 0.40893449289870487, 0.40993555652881186],
        13: [0.42351248201213787, 0.4405305637239567, 0.4328348870675092, 0.4318963899142839, 0.43164612400675717],
        14: [0.4477257085653507, 0.4503535005943815, 0.453857223299756, 0.4462241131201902, 0.4502909341174998, 0.4527310267158856],
        15: [0.45248076080835886, 0.47256459988738037, 0.451855096039542, 0.4763185885002815, 0.47081273853469313, 0.46649565162985673],
        16: [0.4888318838766189, 0.4763811549771632, 0.4755677907777013, 0.4863917912782331],
        17: [0.506788462741663, 0.4898329475067259, 0.4855784270787712, 0.5101044860163925, 0.50778952637177],
        18: [0.5064130638803729, 0.512794844522305, 0.4975911906400551, 0.5152975035975724, 0.48901958330726397, 0.5045360695739223],
        19: [0.5308765563411124, 0.49827942188575364, 0.5323155853093913, 0.5234311455921917, 0.5080397922792967],
        20: [0.5492711005443284, 0.5354439091534756, 0.5526496902959395, 0.5282487643120816, 0.5170493649502597],
        21: [0.5331289495088531, 0.5507101295126071, 0.5492085340674466, 0.5538384533566915, 0.5500844647437902, 0.5500218982669086],
        22: [0.5884377150722643, 0.588687980979791, 0.5613464305824939, 0.573108928236251, 0.5793655759244197],
        23: [0.5779265469561409, 0.5824313332916223, 0.5923168366389289, 0.5991991490959144, 0.5794907088781831, 0.5921291372082838, 0.5994494150034412, 0.6010135769254833, 0.5862478883814053],
        24: [0.571106800976037, 0.6034536695238691, 0.5806794719389351, 0.6049552649690296, 0.6065819933679535, 0.589689044609898, 0.5965713570668836],
        25: [0.6266658324469749, 0.6153413001313897, 0.6167177626227867, 0.5946317962835512],
        26: [0.6364262028405181, 0.6297941562910593, 0.6043296002002128, 0.5942563974222611],
        27: [0.636050803979228, 0.6246011387098792, 0.638052931239442, 0.6452480760808359, 0.6298567227679409, 0.6287930926609523],
        28: [0.6487517987862104, 0.657198273165238, 0.6478758681098667, 0.622661577926547, 0.6279171619846087],
        29: [0.6563849089657762, 0.6548833135206157, 0.6663955452668461, 0.6590752674716887, 0.6722767940937245, 0.6668335106050178], 'file': 2}


file3= {1: [0.05566832436821273, 0.05566832436821273, 0.05566832436821273, 0.05566832436821273],
        2: [0.09316959301735513, 0.09748300010149193, 0.09748300010149193, 0.09748300010149193, 0.09748300010149193],
        3: [0.13127981325484625, 0.13498426875063432, 0.13498426875063432, 0.13498426875063432, 0.13498426875063432],
        4: [0.15036029635643966, 0.17223180757129808, 0.16852735207551, 0.17223180757129808, 0.17223180757129808],
        5: [0.20521668527352074, 0.20151222977773267, 0.19562569775702832, 0.19481376230589667],
        6: [0.22683446665990054, 0.23287323657769207, 0.23287323657769207, 0.23287323657769207, 0.218562874251497],
        7: [0.24352988937379477, 0.26585811427991474, 0.24611793362427686, 0.2549984776210291, 0.25733279204303255],
        8: [0.27504313407084136, 0.27839236780675936, 0.28762813356338174, 0.27169390033492336, 0.28509083527859536, 0.28270577489089616],
        9: [0.28955648025981934, 0.30285192327209987, 0.30280117730640416, 0.27575357759058156, 0.307672790013194, 0.3031056531005785],
        10: [0.3236070232416523, 0.31741601542677356, 0.31660407997564194, 0.3142697655536385],
        11: [0.34192631685780983, 0.3449710747995534, 0.3397949862985893, 0.3397442403328935, 0.34385466355424743],
        12: [0.3559322033898305, 0.35623667918400487, 0.35395311072769714, 0.3473053892215569, 0.337612909773673],
        13: [0.3652187151121486, 0.3680097432254136, 0.3654216989749315, 0.37415000507459656, 0.3726783720694205, 0.3533949051050441],
        14: [0.39373794783314725, 0.38693798842991983, 0.3949558510098447, 0.3873947021211814, 0.39191109306810107],
        15: [0.40708413681112354, 0.3947021211813661, 0.3915051253425353, 0.39363645590175583],
        16: [0.41063635440982443, 0.41911093068101085, 0.4154064751852228, 0.41576169694509285, 0.4016543184816807],
        17: [0.43108697858520245, 0.43595859129199227, 0.4321526438648127, 0.42956459961433063, 0.4328630873845529],
        18: [0.44504211915152747, 0.4497614939612301, 0.449964477824013, 0.44280929666091545, 0.4407287120673906, 0.43443621232112045],
        19: [0.44529584898000607, 0.46031665482594136, 0.4525017761087993, 0.458337562163808, 0.44691971988226936],
        20: [0.46148381203694305, 0.4583883081295037, 0.45864203795798236, 0.47264792449000304, 0.45960621130620116],
        21: [0.47153151324469705, 0.484928448188369, 0.47345985994113465, 0.4771643154369228, 0.47564193646605096],
        22: [0.4798031056531006, 0.4728001623870902, 0.484928448188369, 0.4915761696945093, 0.4858418755708921, 0.4837612909773673],
        23: [0.48431949660002027, 0.501674616867959, 0.5067999594032274, 0.5066477215061402, 0.5096417334821882, 0.5017761087993504, 0.5053790723637471],
        24: [0.5082208464427078, 0.508373084339795, 0.4917791535572922, 0.5090835278595351, 0.5075611488886633, 0.4958388308129504],
        25: [0.5263371561960825, 0.521567035420684, 0.5045671369126155, 0.5226834466659901],
        26: [0.5242058256368619, 0.5202983862782908, 0.5161372170912413, 0.501674616867959],
        27: [0.5346087486044859, 0.5389221556886228, 0.5446564498122399, 0.5346594945701817, 0.532375926113874, 0.5353191921242261],
        28: [0.559525017761088, 0.5497310463818127, 0.5492235867248554, 0.5572414493047803],
        29: [0.5535369938089922, 0.5562265299908657, 0.5526743123921648, 0.5514564092154673, 0.5581548766873033, 0.5551101187455597], 'file': 3}


file4 = {1: [0.04534744326402381, 0.04534744326402381, 0.04534744326402381, 0.04534744326402381],
         2: [0.08941341821338514, 0.08941341821338514, 0.08941341821338514, 0.08941341821338514],
         3: [0.11975528088958703, 0.11975528088958703, 0.1234756727708652, 0.1234756727708652, 0.1234756727708652],
         4: [0.1510065726923236, 0.13600099210450167, 0.14968376669009137, 0.15381753544706708, 0.1510065726923236],
5 : [0.1813484353685255, 0.1726261832913067, 0.1813484353685255, 0.174445041544376],
6: [0.2019759414658344, 0.19842090033483528, 0.1985035757099748, 0.20408416353189202, 0.202554669091811],
7: [0.22293414906370138, 0.2035467735934852, 0.22702658013310736, 0.22859741226075814, 0.21756024967963292, 0.21598941755198214],
8: [0.2469513455417304, 0.24438840891240543, 0.23314455789343144, 0.25046504898515976, 0.25046504898515976],
9: [0.2692736968293994, 0.2541027654912984, 0.25980736637592494, 0.25745111818444877],
10: [0.28742094167252286, 0.2796907940969782, 0.2891984622380224, 0.27324211483609606, 0.28279112066471],
11: [0.29614319374974163, 0.3000702740688686, 0.29787937662767144, 0.30515480963994873, 0.2829978091025588, 0.285519408044314],
 12: [0.30602290107891367, 0.2961018560621719, 0.3115208135256914, 0.3181761812244223, 0.3117688396511099, 0.31329833409119096],
 13: [0.3121822165268075, 0.33032946136993097, 0.3271877971146294, 0.32309536604522343, 0.31623330990864373],
 14: [0.32582365342482744, 0.35070894134182135, 0.341573312388905, 0.33777024513248727, 0.35128766896779795, 0.3383076350708941],
 15: [0.3541399694101112, 0.33901037575958, 0.3490140961514613, 0.3554214377247737, 0.358604439667645, 0.3620768054235046, 0.35612417841345956],
 16: [0.3793146211400934, 0.37290727956678105, 0.375470216196106, 0.3606299863585631],
 17: [0.38258029845810426, 0.3817948823942789, 0.3919226158488694, 0.39035178372121865, 0.3867967425902195],
 18: [0.3829109999586623, 0.3933280972262412, 0.39981811417469304, 0.40688685874912156, 0.4010582448017858, 0.39142656359803235, 0.38803687321731223],
 19: [0.4197842172708859, 0.40535736430904057, 0.409201769253028, 0.4165598776404448],
 20: [0.43425240792030095, 0.4237939729651523, 0.42416601215328015, 0.41974287958331613],
 21: [0.41957752883303706, 0.4211896986482576, 0.4398329957422182, 0.43309495266834774, 0.41449299326195693, 0.4369806952999049],
 22: [0.43218552354181305, 0.4355752139225332, 0.45169691207473855, 0.4406597494936133, 0.44781116944318133, 0.44305733537265923],
 23: [0.4475631433177628, 0.4556239923938655, 0.45136621057418047, 0.4411558017444504, 0.44595097350254226],
 24: [0.4524823281385639, 0.46389152990781696, 0.4504981191352156, 0.47141498904551277, 0.4678599479145137, 0.45587201851928405],
 25: [0.48104667024926623, 0.4809639948741267, 0.47310983423587283, 0.4655036997230375], 'file': 4}

cplex1 = [1097,1763,2256,2723,3162,3541,3892,4233, 4548, 4847, 5129, 5393, 5652,5909, 6153, 6393, 6625, 6855, 7083, 7301, 7516,7716,7911,8099,8287]
cplex2 = [1097,1921, 2587, 3237, 3758, 4257, 4750, 5232, 5671, 6050,6401, 6742, 7057, 7356, 7638, 7914, 8178, 8437, 8694, 8938, 9178, 9410, 9640, 9868, 10086]
cplex3 = [1097, 1921, 2660, 3394, 4060, 4710,5239, 5721, 6150, 6529, 6877, 7219, 7557, 7876,8175, 8470, 8727, 8982, 9235, 9479, 9723, 9963, 10191,10418, 10631]
cplex4 = [1097, 2163, 2987, 3721, 4387, 5037, 5566, 6059,6541, 6996, 7435, 7864,8243, 8594, 8935, 9273, 9592, 9907, 10206, 10505, 10787, 11051, 11310, 11567, 11820]

def plot(a,b,c,d) :
    if a :
        for i in range(1,25):
            for pt in file1[i]:
                plt.plot(i, pt*100, marker='o', color='r', ls='', markersize=2)
        for i in range(len(cplex1)):
            plt.plot(i, (cplex1[i] / 12151)*100, marker='o', color='black', markersize=3)

    if b :
        for i in range(1,25):
            for pt in file2[i]:
                plt.plot(i, pt*100, marker='o', color='b', ls='', markersize=2)
        for i in range(len(cplex2)):
            plt.plot(i, (cplex2[i] / 15983) * 100, marker='o', color='black', markersize=3)

    if c :
        for i in range(1,25):
            for pt in file3[i]:
                plt.plot(i, pt*100, marker='o', color='g', ls='', markersize=2)
        for i in range(len(cplex3)):
            plt.plot(i, (cplex3[i] / 19706) * 100, marker='o', color='black', markersize=3)

    if d:
        for i in range(1,25):
            for pt in file4[i]:
                plt.plot(i, pt*100, marker='o', color='y', ls='', markersize=2)
        for i in range(len(cplex4)):
            plt.plot(i, (cplex4[i] / 24191) * 100, marker='o', color='black', markersize=3)


    plt.show()

plot(1,0,0,0)