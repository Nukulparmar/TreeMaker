import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/2550000/A68A8C8A-689E-5F4D-85A3-817696C6499F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/02BDEF17-26FE-8749-AE0C-C26023BB8B2B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/0568FD2D-BA80-E440-82DA-192D85F6B8B0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/147ED3D2-4C83-5E45-AD60-7E25651DB300.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/156F90EB-B6D9-2044-9A94-8F05CB697EB9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/1874E621-FECF-8946-A0BA-FEDD540CB6A3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/19AEAE9C-2366-E046-AD81-963C72208AB9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/1B3A60AC-EF8E-F547-806B-133FA60D3214.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/1FD745A7-A86C-A840-A7CF-1639A79E6661.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/22A50CB0-D471-4240-9A55-A74B8D5DA056.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/26A6F0DB-A85D-5149-86B7-5C9228D590BE.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/2C0C6B88-9737-864F-B26D-2BA4C9AA3DE4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/3494F574-8D88-4D45-AB9D-D93E6D115964.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/36F09FB8-A594-6D4B-9C11-7F747B086CBB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/38B6F371-9ED9-0D49-B76F-96402E5C815F.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/3A941C22-2F55-7147-A6C3-D8E4B89C30DB.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/3D8BEE0A-6897-C647-A253-02311001E547.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/3DF958A1-818E-804E-93CE-65B225DD7407.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/491A2B43-3975-2648-9819-06C0D0B7A5A9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/49442D5E-3E24-CF42-A734-7BBEEDF5D1E8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/4C0C921C-62C5-0B4C-A212-1F5642EB2E7D.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/4CB8B56C-B7CC-D847-8D42-11D086813053.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/543D4776-7EFF-5F48-AC9E-0E8B332FC297.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/5A7005EC-5FAC-C74B-BB80-49B4B17A2707.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/5BB9E153-1391-A54C-B8D7-4B822FA7C38C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/62ED283C-1F7A-EC41-BE58-7BB2EB4FEFD8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/688A62B2-F3EE-AF4B-AEEC-081789675BF7.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/71D4838F-75CC-EA47-87A5-EB130DBCF61C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/77AF81B6-DBE7-014B-90B4-B655B7B8B7A3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/81F16101-56C6-8847-89C5-5EBECB4BB179.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/833DE8A5-4D77-5949-8BC2-76794B9EBF30.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/8EC19C04-D1B5-704D-8FA5-149B2D826FE8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/915147D1-376B-B64B-93E6-9E88D81D0589.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/92BE1FD3-20DD-F247-A804-57B40F41AAAC.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/9600AD2C-A38F-8D49-BA8C-D83E73D11C55.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/97A8DC28-4231-1446-8B3A-E902678960B9.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/9B563A4D-7780-A344-BDA8-4A059A4D7547.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/9F00568B-2683-6B44-9CF6-45AE54CD766B.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/A0E67C5E-A3F2-0E40-A236-2CAC5B2B75B1.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/A1A365E0-6A0E-0243-A0FF-F9DCB9E530C8.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/A8B3C702-7296-7041-A926-A5ED19A48012.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/A97C4CF7-21BD-4848-A04D-F55FC315C162.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/AFB5DB25-E42E-0D44-907B-8CCC8C6E4DE0.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/BBDB91B7-706D-E845-88B3-ACA26FACF712.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/BD1DF62B-0E5D-E14F-9A51-0728EBFB9F03.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/C06AD42B-A192-B446-AF21-D2B58556C86A.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/C32EBC86-995A-1D40-9CF3-B82CEB6C9266.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/C4A30A63-5BC5-DF44-B396-9C8DF45519D4.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/CA012764-F055-2147-A777-43608F2DFD25.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/D9E7E19E-BECF-1E41-8091-B41B44AC4264.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/DDE3434B-DB32-CF46-946F-5A4BC6DDE635.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/E4222316-C868-6849-834B-158EDF7D0577.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/E6089CAC-4830-8E4B-9DA0-A3A59AC7BFD3.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/EE27BFB4-3D7B-1640-8732-22030EC25159.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/F7F38E65-E797-8F44-AE5E-2BE200D7729C.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/260000/FD047256-1D83-D34C-B0D6-439AD76E5727.root',
       '/store/mc/RunIISummer20UL16MiniAODAPVv2/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_mcRun2_asymptotic_preVFP_v11-v2/270000/36A6BAF3-1AD3-F14B-9420-0CF49E721F6E.root',
] )
