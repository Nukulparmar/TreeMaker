import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/712BA077-AF1C-6243-9FBD-08A777B0695A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/DB37B095-C603-794C-BF69-FDED88BF2544.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/3D88888C-6EC3-9240-9738-0BCA92CFE99D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/184C0E9C-ABF5-034C-B5E3-ED049E9E21BD.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/FF414C32-C9EB-BE45-9196-C68455D03884.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/B9A2F84E-FC3A-8249-835A-E7D982B25C38.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/9711CDD6-1D84-DF4D-8EE5-DDC3AA67E977.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/232F1F5F-9EB3-884D-903C-1F588AC7805B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/304B8B9A-5E83-E14C-86C2-CCD725BE8D4D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/D30D35D4-8319-6F46-B6FD-42BD5331BD67.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/197D9B33-5D47-4E45-8932-FA996C2FFCEF.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/8CB66FD3-FE98-E64D-AA9D-6F20375D98A1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/8099D40E-35DE-2E42-A2DD-5ECF231F05F2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/82FF2798-F0CE-264A-A2BB-72CAF7219896.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/4BD8DC99-FB96-1641-9E38-77F473E21AF5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/8BF1EE55-F489-274C-B5BC-F82F22BF1888.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/441A944E-E048-D04B-A5D4-6A505F400D40.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/653B6E6A-42ED-B54D-B39A-7C7A252E94F6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/194B9F2D-5F47-7644-BC4F-82B5E4093B68.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/E80861F4-7B0D-2745-B2FB-3A3CA40F68F9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/0E5B328F-7ACE-9D42-BBE7-04E67A0CFF31.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/7E9A633D-34F1-EE4F-A882-05EBDA0F7042.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/DE0D1073-54D7-9844-915D-1CCD6E0A7F28.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/24338B0F-9D4F-E945-8250-AF9964184F3A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/C4A09750-2A47-7940-BB44-F2817F763E9A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/B76ACECA-0C3F-EF45-B912-0132E1105F60.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/4F11D034-28C1-9A40-9D7A-12F1BB01A74B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/58ADA729-CDE3-064C-98A4-A7D0D5A5D8D7.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/FFCC5716-C1D6-5341-8CFD-77C1E1D43E97.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/6604BB90-2624-4746-8FC4-1E4518BD39A4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/96827D2D-2EEE-1F45-9BAE-7CD67FA4C6F5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/49E0FD1C-3DFB-E04E-ACF2-D0FBD7F1C23A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/B11A981C-944F-E648-A798-0BDF6622F2F5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/A101411C-B49B-7B47-BA35-3C799B2E0BD4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/075A021C-BB0C-4B4F-A34C-1662963C5DE9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/8380F691-BF48-194D-8088-889E71A87735.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/31A88521-58BE-9A45-8EE3-11A641B447D5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/1715942A-EA8C-C94C-9B1C-CA1CC249BD37.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/91049580-17DE-DA4E-A69F-60A4DE27D945.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/525C1BE9-FBB8-E846-AB07-B76969DAC4B8.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/BB48DF29-027D-2544-8D78-39913899B84A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/3DCF7785-931E-1C4C-895A-399D0D57AC5C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/CA45302C-7E2A-EF4F-A194-0132A8862BFA.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/B0746011-596F-6A4B-817C-07969E020B63.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/F92B7BBD-7747-BB44-B621-A13D4A6103CF.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/F3591010-E3CF-F846-8EAD-73669BCFE853.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/A7F7E773-168A-B34E-BA0D-47A8BB5AFD33.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/A8263962-A36C-3D46-A7E5-D8EF71C458EA.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/9794AED4-828C-B34C-908B-379084934630.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/DC7D7299-3237-7947-A1D9-36B3360A9B51.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/E39B52F7-2CE8-0744-A54F-A61A593B5E2B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/3CCC01B8-4899-7847-9368-469DC8B9620F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/FE523D62-25A0-254F-9532-C778EF005748.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/504867EA-664C-534C-A58A-866DCA6962F1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/B35150AA-CE1F-F840-9B49-F9F7B2419FAD.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/BCF761F7-6CCF-1D49-B408-5FC0F9A23F00.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/49B8D30A-A598-1649-B969-F2E4277C46F7.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/81DCBC63-A882-F844-8EEF-6E3C58DB404C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/BAE650E7-4DBD-9242-B94B-DF0A73FAA97E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/CBAE212B-2691-FF4E-AB1F-CC9D66ED890A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0C192E3F-DCA8-7946-A589-62314F5D1940.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/49DCE1B5-43DC-9444-BD24-2C35C5AC0EE8.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/E476288F-12EC-3D41-BA86-AA4BE355E254.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D9EFF455-B1F9-4D47-8CDE-F3D1A657FCBA.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/17B3C7BA-B09D-2B46-B1F1-DACA7BE93EA8.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/5104A3A3-7CC9-BA4B-BEB3-09E312ED9DCF.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/91F3E1AF-5BD6-1149-B6E8-84EBE0B5FA27.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/EBB39B80-41D5-0447-A5BE-265BCB975B43.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/7D10BCF7-F714-4042-AC06-135CE95256AA.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/F5877868-9C41-0743-893C-41209536AE04.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/10AB948C-9539-8749-913B-0245712036F4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/829D41BF-5F7B-2248-A560-76FEA7191AC5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/6F21D576-ECDD-2843-B4AF-5641968D2F71.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/20E3BAA3-8339-4A41-B79F-177F6BD7DA94.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/73AF0A2E-57B4-1649-B9C4-38298DDFC2EB.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/E177A115-C2D8-5549-9EC4-27B8E4246CD3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/3284E79F-6E9F-974F-8F56-B68B2B911796.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/9F4530F2-D888-414D-B042-94A452E45D5F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/39959D83-B138-4347-AF33-CDA707255548.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/CE913439-1907-F14D-935C-78DAE8DB6803.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/CB29245A-20E6-494F-A562-8313A6E3CFBD.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/DC72CF70-687F-094F-9FEE-854841FF1029.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/738F5891-6E17-3D49-8313-EA931D0F927D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/0B3BFE72-ED4D-3342-88E0-5841F1498EBE.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/85B9707D-5913-334E-B71D-675F681C3985.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/63599234-A340-2547-87A1-FD7D1028B107.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/E25EBAC0-63C7-3744-A553-7B2CC37D93E1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/8B8C7476-0BB2-8447-B345-BB432F01C39F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/0C6A7574-2DCB-264E-894E-6EAB06FD777D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/81B3F346-AAB2-A942-9653-B9018D80D1F3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/A6F15658-AED7-3041-9811-0B031A653342.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/C16584F2-D56A-724C-9914-1100D4CA8283.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/7F22A111-2270-CB4C-A592-B1165067626B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/8E94E698-CB49-D54C-A385-38A2747948B0.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/67729476-D6ED-2941-A5E9-AF50F00EC473.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/18DF4841-D73A-2D4F-94DB-7BB6BD314B62.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/0D24114B-57C8-664D-AE97-CAC407B475EB.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/D023764E-E7E9-2543-A531-C1AA5FB13AEB.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/78681046-2891-7D47-B059-7B6203D344FD.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/5450B219-8691-2545-A02D-C382D39911D3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/47445DDC-7F00-7D48-A6CB-32DC274BC04E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/AFDEBD2D-CCEA-E54B-878F-6FC55AB2AD56.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/079E5AD2-0575-6E4C-A218-B127E36874E4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/E20E6CBD-ABBA-9C45-9EF9-35E99D634016.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/6BF797B9-BD45-E24B-A63F-4A24ED636AE2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/51154C65-6ED1-364E-AD6C-2588CC7BAB24.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/FC0FC973-A5F2-9C45-A538-54F76F16DF32.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/17027990-68B7-BD49-8BA1-C4E9D00A020C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/62075359-8766-A448-9402-8473943D0FED.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/8BA5AAC0-4CE8-3F40-A0A6-59A5D3E25248.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/EC4E2CBF-C89B-634B-BF3E-266CAA367DD1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/ECBA2733-A674-EE42-B411-E043BD26DCF9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/AA0BC6FB-8448-AA44-91F9-D8B7AEE5541F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/75E5D80C-46D4-2644-97A1-CDBCDBB9ABE2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/161B9AA8-2DBF-CD4B-BC45-C4585D3D3529.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0FE9CDBB-D138-D54E-95C2-66B426015D15.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0B4A49F8-10CC-C845-9C88-FB6C9A2742B3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0F2A6F3E-B48D-7549-8576-BD021B241624.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/CF57A6F8-4358-ED4B-A256-2EBCD957FD83.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/A92A22BD-4A01-6C48-8C26-46F78194A444.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D55E72E1-0722-354D-AEF3-EEC2A1557DDD.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/B264D320-9EFD-F648-A3DF-B6E8C75264C5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/666B1C6C-C9D1-D847-8C09-7E628C21D9A3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/18785154-247D-234A-ABAA-5616B5B16770.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/5126194F-CF87-6F4B-A564-33930D7F0A2D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0498A903-1661-8843-917D-0D49CE078A5D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/089F4EE0-965C-5143-89DF-7A7157ED783C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/8DB103E5-49B7-3E41-B617-525157EF84E4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0EA78F3B-829A-1F48-AB1E-62E904F21F97.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/38C855DE-E32B-CC49-BF5A-3F3C62872E37.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/C050CC18-C04E-CD4E-B916-370AB3F191A4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0081791D-FC7A-B740-BB42-335A1E076042.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/AEDD24F5-23ED-904B-B320-DB0EAF2681B1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/EF59F48B-C3FD-494D-85C0-8ADCD6C76EBC.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/8E37AEE6-90D6-EE42-AF0D-FCB6041DFC6E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/69B1FFA8-AD99-8748-A277-22BDC3D5F17E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/3DDA5147-0CD3-6848-B1BF-E3643B607CB9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/6CB88C79-4F2D-184D-A60D-8F1DC0F1C3D6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/3EE8A265-2528-8C47-8F75-2B2260449A2E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/3686BECC-0185-D440-99F8-D27C78168842.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/18BB71DB-E924-184C-B7C3-4FC6D16B9F21.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/ADFE4CE3-9B2C-F94C-BE6F-7EE4164E5F88.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/F60D6CE5-B6FB-134C-87C8-309A8C11E092.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/426A20AD-75AD-F24B-81BC-815B5052F5B7.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/20570E7B-BA5B-DB43-9B8C-0EEF8311000D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/E9F9F34B-7CC0-1D4C-9432-3EC24E7D1771.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/786F31ED-CB24-CB4C-BFF9-34ACEDA24B5A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/08010CB2-15F9-F842-A312-0F873BF6FB88.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/58F34E37-7C72-2945-810D-EDB7FDC0DF75.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/25FB2037-94FD-4247-B516-0FA3E0D9EED4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/787471E9-62DF-E84D-91C6-F739BEE16507.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/C772873B-6670-DE4A-BA80-EA7ACF8A45D0.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/6CA913C0-D377-9447-B093-E0175E248710.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/D95DDD50-A9E2-AF45-9732-111711A05AF2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/86607483-509C-F642-84EA-B4C112ECCFBC.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/44356EA9-C1C4-554B-B2B9-4E454B073C2B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/DB339E1C-3395-884A-9A77-EBC003479767.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2500000/8FA772D4-92D8-0646-BAA2-72501F642A17.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/60061E71-2557-D743-8F4E-F6A9468813C3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/C224DE38-AD3E-AD4C-AB87-6867D6B4DF17.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/BD673BD9-B83E-1C4C-B685-84C3C13E7537.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/ED2FE43A-BA11-444E-8DCC-45C445994FE9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/1709FD90-8E0F-2E4A-BD29-1ED1610D1E69.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/BD5533B5-6EE1-FD42-BEED-345210D61C71.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/64D653F4-C935-AD4A-AFE5-5B239159DC97.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/8B53A0A6-D6DD-3948-8FAD-589B3E6C0ED7.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/E534AE83-95DD-F043-BBBD-ED21A6F2D225.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/17A2B6C3-6807-4442-890B-B3476AD2AF3E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/09624248-2A67-1B4E-84FF-0849F396857D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/4E768D4D-8F58-4C42-B8A4-5993E73C55F6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/70F0A895-1E62-8042-BB64-48F1DEEDADE2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/124FCDD8-2834-F347-9F86-E6BE23740B8F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/65CCEC49-48AE-6B44-A837-493849291983.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/3DCB2A98-9C30-5C48-A880-D13D2085C67D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D649FFB0-8E5F-614A-91E6-77F54D4BD5A4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/23AC5E55-7B7B-2643-AFAE-64855D0440EC.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/3C73EB0C-45C2-464B-A9E5-661B7C021ED9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/58076365-317E-5B4D-9A46-50D1D1AC199E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/FAABAD81-68DD-C64A-8EC7-F01DA0745951.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/EF8F04CE-22E2-B447-B5DA-91DDF7DC31C1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/07F46E02-9854-8B46-9BE7-45E00855853C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D1B49813-FE59-A442-AF78-41A74C95C4F4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/2590C0CA-E6D8-FA4F-9269-F52094CDCF8B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/B05CC210-1471-0B42-AD17-4F8CB1A4B0B1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/DBAB5FC5-9E92-F248-B330-6D2C0B0132E6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/66077566-94FF-2940-8E20-7092D3AB1D5A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/FF969191-7CE3-4741-B87D-8032CFD4F356.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/CD19BDAC-1222-CA49-8494-5DD6E4F9E285.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/9C179E9D-F4D5-A84E-A264-14ECDDFF9BC9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/266C6817-68BE-D945-BCE2-86BB2A398E1E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/008514AE-B02B-AD44-B6CE-7B90EE89CC5B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/91C954FA-A2A6-CA41-AF13-99B4C9BA86D3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/FAED9DC0-6234-D14E-938A-8350B3FF242F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/25FDB5DB-90E8-7A4E-AAA9-1D78FF64D6CE.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/8622EBE2-3CC9-DA4C-AA38-5626AC716AE1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/9C483CB3-4FAE-9C44-B217-E018204EB29F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/DB0C94BD-F0D4-8F4E-8F59-C2DD3FE853B6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/7E9D265E-7C93-664A-A2CE-6B321738255A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/5DE6CA41-1144-7E47-AA9C-EE289D23E0AB.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/C7141379-08EA-394C-9844-3A27EBBCECED.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/A5FE1AA4-B987-1346-841D-6D6F0A7C619D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D2C87337-3F2E-FC4F-9058-9841D3FCD2D0.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/DAD2CA57-B0CE-A840-BE44-73787C329FB3.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D96E1365-7A21-E943-BB21-AE2EB041AA7A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/94CC8860-67A1-3E49-83A3-1F48330B0BA4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/91E174D4-7B29-C845-A988-CBB775E2C672.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/A0246E6F-2315-C940-8232-F8ECCA16A7D7.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/03D22844-AA62-ED41-8AC4-9BADF5903491.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/35A6351A-0092-B047-AA97-8BD34422FEE9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/05BD8F2E-79B4-D24C-9487-A776D48C207E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/28BC8772-818F-F24A-9B4F-AC65E1C9CB11.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/314908CE-F4C4-8940-99C1-60D936A67B06.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/79C95F39-B8A2-F24A-9183-9B19B2FA29CB.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/EDFC07D1-259D-8849-856D-B097490FEC44.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/A9B3CC3E-9692-424F-8058-6716008C1795.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D3A4A6D7-5673-0243-B321-94083C71D2E5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0002F388-FA4E-DE4C-9FBF-08188DBAD1D2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/B3E7CB3D-D485-BE45-A3CE-CBAD404FFE61.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/269214CA-6009-104B-80CA-2731333269DE.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/7D5BED18-B1D0-2D4D-B0B7-AA8ED4264C73.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/58D89ACA-D9D9-7441-89C2-927BB19A1C98.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/BEE505DD-A01F-AA42-93F9-7A9BF5F95D94.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/B738B77B-0769-6F48-8FD4-828A0C2417FC.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/9450C3C7-67B1-884C-B8A5-CCD7F534B5B0.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/4240FF1D-DBCC-444B-8663-DB5BD43D07A6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/0B82748E-0D6A-5841-8300-9FA045596C8C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/667C80F4-2496-9547-91F6-7E2E6ACCE873.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/8EA54118-FE56-274F-A832-5E05C94ADE7B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/70823A45-1296-C448-9958-508E63DDA578.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/AE6FCEFB-0A04-9F4D-978E-40CC6D2C42FB.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/8BC33C5D-03CC-8044-817A-EEC8F55F5693.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/BF076972-20A7-1C47-BB3D-EA6BCE87CA26.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/D9F908D5-8A9E-3A44-AFB1-DBF0C1D37FBC.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/C8102462-0DE5-AB4F-AB4F-DE4290F96C92.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/2430000/E87849FD-B9D6-604A-A820-C2B1DEDE8903.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/C999032D-9F0B-9E49-A9F5-48010CC55142.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/3A7A7864-D9F7-B14C-94A5-E10048D797A5.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/52BECBB1-9732-7041-BBE8-6424069E5307.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/4E594013-6FE3-034E-AD51-D8A475B01FFA.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/A435D082-76C5-5944-B362-B0BE559A73C8.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/8DC435FC-32D3-784A-A734-56B989349C06.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/D0E7454B-56CF-CE4B-88B3-A62F3316EDED.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/7B2C2587-42E2-5741-AE42-DB0D7814E5CD.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/4A6DA645-86BC-EA45-B6F1-4BDF5D2756CC.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/AA142E88-901C-E040-BB73-5F231CD45521.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/BEE4A603-4D25-DB40-B178-5852F69FB14E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/97A68EC6-8658-3B46-BD1E-F82F9B195B61.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/6E4A0FEB-CD4B-9241-B3D7-1BF43196634F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/8D1F1EE2-E041-A946-9C12-580DB1C06AEF.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/EA29D972-4009-A241-ADE9-F381CEB29C26.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/C8FA7118-39F6-0244-848D-A3A0C51B14CB.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/1EC8F424-E569-F642-8B81-2BBC0A3983EA.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/22E290DE-DA32-2940-A937-DD659412ED1F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/558F5E51-7177-7644-9FD6-D05419FC618A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/6675A7D2-43E0-5C49-A802-B0DD20FFD75E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/FF405F60-325E-BE4E-88E3-BC1702128E58.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/9CAB6B62-A2B9-7C48-8731-0FF842E06F7F.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/47354F0F-9B32-9E4C-9C81-EC28CEE12301.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/66DABBB7-9397-B248-8C6D-8FDD68CAEF2E.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/2D516442-B04F-5149-98D7-1A556FDB1EA7.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/F608D116-C415-8748-BECA-B9F73BA97BA0.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/CB71D8C6-C04A-3246-BA74-ABB1B85F2535.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/3A9F68F6-597B-C84C-AADC-42508CE27BE4.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/0A4450A1-F195-A844-985E-266944BF4B79.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/65DA6CAE-BDDE-7B43-BB71-E69BF1A974D2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/1E1B63C1-717D-114E-9E59-CF467E1762FF.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/5203E319-72EF-3440-816E-FFBC0E0B3A45.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/286D1417-1052-E841-868B-C5CA10451EE2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/4CF739AD-DB28-0E44-BA7F-01DBC37D21ED.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/3622F645-A64C-1244-9F7F-13C1B9E34E46.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/F7BD8E7B-5860-904E-8917-CDC0DA4297E0.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/B2BC55C7-602B-294E-A0CC-0D398720493D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/7BCE0D01-ACEF-4642-850D-12020D7C5BD9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/71955682-A1C1-6C43-845D-4C7DBA6BDE90.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/02EF8A4F-DE5F-974A-89BF-73C6830EC012.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/73A12D0D-393E-C94D-B9E0-7D57674FFE86.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/9587DC06-3EC5-534B-919D-B062EB73AE84.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/30ED46B3-86B8-BC4B-AE47-88C06205973B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/D3FBE447-E323-D149-BADF-5A885C34D506.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/DD6D3E57-8C39-3046-8C01-CEF8A0089387.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/4D422188-74C4-5046-9CAC-8DA1975FFAA6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/D201DF4E-5FE6-224C-A1EF-417EDE4E654C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/3EE75CD7-DADE-234F-9502-3F01EC510D73.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/97AF57A9-0B48-EF4C-B115-81D5D2E190A9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/DB3D508A-732F-6041-9DF6-4766CD0C8DB9.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/37E01E26-F226-8249-A93D-6AE275D117FF.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/B0647FBC-AB80-D344-8A2E-90880CD6C746.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/A3143FFC-26AF-7348-A98A-2BE87418C702.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/34C7AD2C-5694-4443-907C-C1D5DB3D754D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/E0B80057-ED88-AD45-A453-C8B992FAD7C2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/6ECB4E02-23B2-D247-B303-ED1B7C460AF6.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/BC6D8C5E-A794-B44D-85B8-2450242A1D7D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/6C025013-0C2B-1A4D-84FC-005AF6E33EC0.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/67EE57D0-F39D-A74E-A19C-F828700252AE.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/C9E47014-DE29-BD49-AE6C-9E481FB01284.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/390E7361-EE71-724E-BD35-B0573985B80B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/8DBB5B47-9013-8C45-B599-C4B050B0A088.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/250000/54907DB0-5E08-3248-9994-DB6DD3162E20.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/55ECE38B-7B41-6A47-B081-14AC71870871.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/A06BA931-E82A-E647-B003-CF91CC5C1CEA.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/66264423-5698-F640-A1FE-31B75E9E9E58.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/B69FB682-D048-234F-810F-0572C97D8E9D.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/0362C9F6-1B01-E84E-AEAE-FF0CCC311A8A.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/F09346B3-D4F6-F947-902F-ADE19FB79AE1.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/95EA561B-5968-8D4A-9A72-0CFA5887EA90.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/8A9EB10C-0A09-354D-A254-7E18A03A2FFD.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/58E34B3F-6920-E148-8E2F-CEC5639EAB4B.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/AE93CCE4-FE73-3C48-91CE-2C2F1672AB60.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/3193A822-7FED-0541-934C-75763A9B5E70.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/D44020A6-641A-D248-86D5-1D0FCC06D9B2.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/411994E0-B506-B649-B10E-A8E020F70110.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/85DD3D4B-56B1-7C42-8939-24457FE0962C.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/4BDDA8EA-DBED-4743-8EB5-4F5A7C246ADC.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/A40908D5-91E9-6B4C-8612-C1C0759A87EF.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/08D37172-45A9-9040-B3A2-5D75A2C82499.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/37C9D0A6-8830-AD4B-872C-1B8D0B46B5ED.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/25C3B31D-D92C-2044-B8F2-A9EBE3588474.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/25168E92-2E9D-2F43-A694-6E662E372894.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/349D92EE-9E5F-FD40-8015-5C1B5B7A8232.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/9EC2F78E-E4F6-C346-ADBB-81CACDF92EAE.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/100000/931140C6-8706-704E-AB24-7DA0C554A458.root',
    '/store/data/Run2016G/SinglePhoton/MINIAOD/UL2016_MiniAODv2-v3/430000/1685F00E-7749-B746-98F6-410FE9CA6ABB.root',
] )