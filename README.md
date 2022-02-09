# An MVP project to showcase literacy with BeautifulSoup, re, PrettyTable and custom Data Models.
One can run this via the following command:

```
python3 main.py https://www.imdb.com
```

Please note that you have to provide a link as the command line argument. 

## The output of the program is as follows

```
❯ python3 main.py https://www.imdb.com                                  
Please provide a keyword if you'd like to search for it: movie
+----------------------+-------------+----------+----------------+------------------+---------------+
|         URL          | Status Code | Encoding |  Elapsed Time  | Contains Keyword | Keyword Count |
+----------------------+-------------+----------+----------------+------------------+---------------+
| https://www.imdb.com |     200     |  utf-8   | 0:00:00.913854 |       True       |      181      |
+----------------------+-------------+----------+----------------+------------------+---------------+
+-----+------------------------------------------------------------------------------------------------------------------------------------+
|  #  |                                                                Link                                                                |
+-----+------------------------------------------------------------------------------------------------------------------------------------+
|  1  |                                                           /?ref_=nv_home                                                           |
|  2  |                                           https://www.imdb.com/calendar/?ref_=nv_mv_cal                                            |
|  3  |                                                 /list/ls016522954/?ref_=nv_tvv_dvd                                                 |
|  4  |                                                     /chart/top/?ref_=nv_mv_250                                                     |
|  5  |                                                 /chart/moviemeter/?ref_=nv_mv_mpm                                                  |
|  6  |                                                   /feature/genre/?ref_=nv_ch_gr                                                    |
|  7  |                                                  /chart/boxoffice/?ref_=nv_ch_cht                                                  |
|  8  |                                                     /showtimes/?ref_=nv_mv_sh                                                      |
|  9  |                                      https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth                                      |
|  10 |                                                    /coming-soon/?ref_=nv_mv_cs                                                     |
|  11 |                                                     /news/movie/?ref_=nv_nw_mv                                                     |
|  12 |                                                   /india/toprated/?ref_=nv_mv_in                                                   |
|  13 |                                                   /whats-on-tv/?ref_=nv_tv_ontv                                                    |
|  14 |                                                   /chart/toptv/?ref_=nv_tvv_250                                                    |
|  15 |                                                  /chart/tvmeter/?ref_=nv_tvv_mptv                                                  |
|  16 |                                                          /feature/genre/                                                           |
|  17 |                                                      /news/tv/?ref_=nv_nw_tv                                                       |
|  18 |                                                      /india/tv?ref_=nv_tv_in                                                       |
|  19 |                                                   /what-to-watch/?ref_=nv_watch                                                    |
|  20 |                                                      /trailers/?ref_=nv_mv_tr                                                      |
|  21 |                                                     /originals/?ref_=nv_sf_ori                                                     |
|  22 |                                                       /imdbpicks/?ref_=nv_pi                                                       |
|  23 |                                                       /podcasts/?ref_=nv_pod                                                       |
|  24 |                                                      /oscars/?ref_=nv_ev_acd                                                       |
|  25 |                                       https://m.imdb.com/feature/bestpicture/?ref_=nv_ch_osc                                       |
|  26 |           https://www.imdb.com/search/title/?count=100&groups=oscar_best_picture_winners&sort=year%2Cdesc&ref_=nv_ch_osc           |
|  27 |                                                       /emmys/?ref_=nv_ev_rte                                                       |
|  28 |                                            /imdbpicks/blackhistorymonth/?ref_=nv_ev_bhm                                            |
|  29 |                                                  /starmeterawards/?ref_=nv_ev_sma                                                  |
|  30 |                                                    /comic-con/?ref_=nv_ev_comic                                                    |
|  31 |                                                       /nycc/?ref_=nv_ev_nycc                                                       |
|  32 |                                                     /sundance/?ref_=nv_ev_sun                                                      |
|  33 |                                                      /toronto/?ref_=nv_ev_tor                                                      |
|  34 |                                                  /awards-central/?ref_=nv_ev_awrd                                                  |
|  35 |                                                  /festival-central/?ref_=nv_ev_fc                                                  |
|  36 |                                                     /event/all/?ref_=nv_ev_all                                                     |
|  37 |                                                /feature/bornondate/?ref_=nv_cel_brn                                                |
|  38 |                                        https://m.imdb.com/chart/starmeter/?ref_=nv_cel_brn                                         |
|  39 |                                   https://www.imdb.com/search/name/?match_all=true&ref_=nv_cel_m                                   |
|  40 |                                                  /news/celebrity/?ref_=nv_cel_nw                                                   |
|  41 |                                            https://help.imdb.com/imdb?ref_=cons_nb_hlp                                             |
|  42 |                                          https://contribute.imdb.com/czone?ref_=nv_cm_cz                                           |
|  43 |                                                        /poll/?ref_=nv_cm_pl                                                        |
|  44 |                                         https://pro.imdb.com?ref_=cons_nb_hm&rf=cons_nb_hm                                         |
|  45 |                                                           /?ref_=nv_home                                                           |
|  46 |                                                    https://www.imdb.com/search/                                                    |
|  47 |                   https://pro.imdb.com/login/ap?u=/login/lwa&imdbPageAction=signUp&rf=cons_nb_hm&ref_=cons_nb_hm                   |
|  48 |                                                /list/watchlist?ref_=nv_usr_wl_all_0                                                |
|  49 |                                              /registration/signin?ref=nv_generic_lgin                                              |
|  50 |                             https://help.imdb.com/article/issues/G6TCMBKAAR5G95EN?ref_=loc_nav_sel_hlp                             |
|  51 |                                     /list/ls053181649/videoplayer/vi2617951001?ref_=hp_hp_e_15                                     |
|  52 |                                     /list/ls053181649/videoplayer/vi1393214233?ref_=hp_hp_e_1                                      |
|  53 |                                      /list/ls084858008/videoplayer/vi671859481?ref_=hp_hp_e_2                                      |
|  54 |                                     /list/ls053181649/videoplayer/vi2869674777?ref_=hp_hp_e_3                                      |
|  55 |                                     /list/ls084858008/videoplayer/vi1577763609?ref_=hp_hp_e_4                                      |
|  56 |                                     /list/ls053181649/videoplayer/vi1912783641?ref_=hp_hp_e_5                                      |
|  57 |                                                      /trailers/?ref_=hm_hp_sm                                                      |
|  58 |         /family-entertainment-guide/2022-tv-guide/ls513911205/mediaviewer/rm558096641/?ref_=hm_edcft_wot_tvguide_ft_c_1_i          |
|  59 |         /family-entertainment-guide/2022-tv-guide/ls513911205/mediaviewer/rm558096641/?ref_=hm_edcft_wot_tvguide_ft_c_1_t          |
|  60 |                                     /oscars/nominations/?ref_=hm_edcft_mobi_oscars_22noms_2_i                                      |
|  61 |                                     /oscars/nominations/?ref_=hm_edcft_mobi_oscars_22noms_2_t                                      |
|  62 |           /oscars/fan-reactions-oscar-nominations/ls539734205/mediaviewer/rm2725832449/?ref_=hm_edcft_ft_oscars_fan_3_i            |
|  63 |           /oscars/fan-reactions-oscar-nominations/ls539734205/mediaviewer/rm2725832449/?ref_=hm_edcft_ft_oscars_fan_3_t            |
|  64 |                            /video/vi2936455961?listId=ls084858008&ref_=hm_edcft_org_sc_blacksupers_4_i                             |
|  65 |                            /video/vi2936455961?listId=ls084858008&ref_=hm_edcft_org_sc_blacksupers_4_t                             |
|  66 |                              /gallery/rg1624939264/mediaviewer/rm2856381697/?ref_=hm_edcft_ph_lp_5_i                               |
|  67 |                              /gallery/rg1624939264/mediaviewer/rm2856381697/?ref_=hm_edcft_ph_lp_5_t                               |
|  68 |                              /gallery/rg1641716480/mediaviewer/rm3947097345/?ref_=hm_edcft_ph_pwl_6_i                              |
|  69 |                              /gallery/rg1641716480/mediaviewer/rm3947097345/?ref_=hm_edcft_ph_pwl_6_t                              |
|  70 |         /family-entertainment-guide/lgbtq-power-couples/rg3163593472/mediaviewer/rm2110191873?ref_=hm_edcft_wot_lgbtq_7_i          |
|  71 |         /family-entertainment-guide/lgbtq-power-couples/rg3163593472/mediaviewer/rm2110191873?ref_=hm_edcft_wot_lgbtq_7_t          |
|  72 |                               /list/ls063853872/mediaviewer/rm3032674049?ref_=hm_edcft_pks_renew_8_i                               |
|  73 |                               /list/ls063853872/mediaviewer/rm3032674049?ref_=hm_edcft_pks_renew_8_t                               |
|  74 |                                                  /what-to-watch?ref_=hm_watch_btn                                                  |
|  75 |                                             /what-to-watch/top-picks/?ref_=hm_tpks_sm                                              |
|  76 |                                         /what-to-watch/from-your-watchlist/?ref_=hm_wls_sm                                         |
|  77 |                                          /what-to-watch/fan-favorites/?ref_=hm_fanfav_sm                                           |
|  78 |                                          /what-to-watch/watch-guides/?ref_=hm_watch_wchgd                                          |
|  79 |                                             /what-to-watch/popular/?ref_=hm_watch_pop                                              |
|  80 |                               /video/vi1192936217?listId=ls025720609&ref_=hm_edcio_org_nsp_halle_1_i                               |
|  81 |                               /video/vi1192936217?listId=ls025720609&ref_=hm_edcio_org_nsp_halle_1_t                               |
|  82 |                             /video/vi941146905?listId=ls025720609&ref_=hm_edcio_org_wtw_febseries_2_i                              |
|  83 |                             /video/vi941146905?listId=ls025720609&ref_=hm_edcio_org_wtw_febseries_2_t                              |
|  84 |                             /video/vi2265170713?listId=ls025720609&ref_=hm_edcio_org_burnq_jackass_3_i                             |
|  85 |                             /video/vi2265170713?listId=ls025720609&ref_=hm_edcio_org_burnq_jackass_3_t                             |
|  86 |                                      /video/vi2533737241?listId=ls535460930&ref_=hm_edcio_4_i                                      |
|  87 |                                      /video/vi2533737241?listId=ls535460930&ref_=hm_edcio_4_t                                      |
|  88 |                              /video/vi388547353?listId=ls025720609&ref_=hm_edcio_org_wtw_22scifi_5_i                               |
|  89 |                              /video/vi388547353?listId=ls025720609&ref_=hm_edcio_org_wtw_22scifi_5_t                               |
|  90 |                                /video/vi671859481?listId=ls084858008&ref_=hm_edcio_org_ros_kasi_6_i                                |
|  91 |                                /video/vi671859481?listId=ls084858008&ref_=hm_edcio_org_ros_kasi_6_t                                |
|  92 |                            /video/vi2936455961?listId=ls084858008&ref_=hm_edcio_org_sc_blacksupers_7_i                             |
|  93 |                            /video/vi2936455961?listId=ls084858008&ref_=hm_edcio_org_sc_blacksupers_7_t                             |
|  94 |                                /video/vi1929823001?listId=ls025720609&ref_=hm_edcio_org_horo_aq_8_i                                |
|  95 |                                /video/vi1929823001?listId=ls025720609&ref_=hm_edcio_org_horo_aq_8_t                                |
|  96 |                           /video/vi4246520601?listId=ls025720609&ref_=hm_edcio_org_fanq_kristenbell_9_i                            |
|  97 |                           /video/vi4246520601?listId=ls025720609&ref_=hm_edcio_org_fanq_kristenbell_9_t                            |
|  98 |                               /video/vi1577763609?listId=ls084858008&ref_=hm_edcio_org_nsp_gugu_10_i                               |
|  99 |                               /video/vi1577763609?listId=ls084858008&ref_=hm_edcio_org_nsp_gugu_10_t                               |
| 100 |                              /video/vi2233254681?listId=ls084858008&ref_=hm_edcio_org_ros_alisha_11_i                              |
| 101 |                              /video/vi2233254681?listId=ls084858008&ref_=hm_edcio_org_ros_alisha_11_t                              |
| 102 |                             /video/vi4228039449?listId=ls025720609&ref_=hm_edcio_org_fanq_pamtom_12_i                              |
| 103 |                             /video/vi4228039449?listId=ls025720609&ref_=hm_edcio_org_fanq_pamtom_12_t                              |
| 104 |                             /video/vi3104293657?listId=ls025720609&ref_=hm_edcio_org_brf_wakanda_13_i                              |
| 105 |                             /video/vi3104293657?listId=ls025720609&ref_=hm_edcio_org_brf_wakanda_13_t                              |
| 106 |                             /video/vi2114306841?listId=ls025720609&ref_=hm_edcio_org_moonfall_qa_14_i                              |
| 107 |                             /video/vi2114306841?listId=ls025720609&ref_=hm_edcio_org_moonfall_qa_14_t                              |
| 108 |                                                    /showtimes/?ref_=hm_inth_sm                                                     |
| 109 |                                                  /chart/boxoffice/?ref_=hm_cht_sm                                                  |
| 110 |                                                  /title/tt11466222/?ref_=hm_cht_1                                                  |
| 111 |                                                  /title/tt5834426/?ref_=hm_cht_2                                                   |
| 112 |                                                  /title/tt10872600/?ref_=hm_cht_3                                                  |
| 113 |                                                  /title/tt11245972/?ref_=hm_cht_4                                                  |
| 114 |                                                  /title/tt6467266/?ref_=hm_cht_5                                                   |
| 115 |                                                  /title/tt6856242/?ref_=hm_cht_6                                                   |
| 116 |                                                    /coming-soon/?ref_=hm_cs_sm                                                     |
| 117 |          /imdbpicks/best-movies-and-tv-february-2022/ls536659052/mediaviewer/rm339468545?ref_=hm_edcep_ft_febpks_wtw_1_i           |
| 118 |          /imdbpicks/best-movies-and-tv-february-2022/ls536659052/mediaviewer/rm339468545?ref_=hm_edcep_ft_febpks_wtw_1_t           |
| 119 |                                           /list/ls532973486/?ref_=hm_edcep_wtw_prime_2_i                                           |
| 120 |                                           /list/ls532973486/?ref_=hm_edcep_wtw_prime_2_t                                           |
| 121 |                                          /poll/7yDy-fwR3vM/?ref_=hm_edcep_pls_020422_3_i                                           |
| 122 |                                          /poll/7yDy-fwR3vM/?ref_=hm_edcep_pls_020422_3_t                                           |
| 123 |                                         /list/ls534728274/?ref_=hm_edcep_pks_febtv_ft_4_i                                          |
| 124 |                                         /list/ls534728274/?ref_=hm_edcep_pks_febtv_ft_4_t                                          |
| 125 |                              /gallery/rg1641716480/mediaviewer/rm3947097345/?ref_=hm_edcep_ph_pwl_5_i                              |
| 126 |                              /gallery/rg1641716480/mediaviewer/rm3947097345/?ref_=hm_edcep_ph_pwl_5_t                              |
| 127 |                                           /list/ls534762477/?ref_=hm_edcep_wtw_hulu_6_i                                            |
| 128 |                                           /list/ls534762477/?ref_=hm_edcep_wtw_hulu_6_t                                            |
| 129 |                                          /list/ls534507123/?ref_=hm_edcep_wtw_netflix_7_i                                          |
| 130 |                                          /list/ls534507123/?ref_=hm_edcep_wtw_netflix_7_t                                          |
| 131 |                                            /list/ls532553515/?ref_=hm_edcep_wtw_hbo_8_i                                            |
| 132 |                                            /list/ls532553515/?ref_=hm_edcep_wtw_hbo_8_t                                            |
| 133 |                                          /list/ls536224688/?ref_=hm_edcep_wtw_disney_9_i                                           |
| 134 |                                          /list/ls536224688/?ref_=hm_edcep_wtw_disney_9_t                                           |
| 135 |                                 /gallery/rg4284128000/mediaviewer/rm346941185/?ref_=hm_edcep_10_i                                  |
| 136 |                                 /gallery/rg4284128000/mediaviewer/rm346941185/?ref_=hm_edcep_10_t                                  |
| 137 |          /family-entertainment-guide/disney-plus-picks/ls092677739/mediaviewer/rm3322936833?ref_=hm_edcep_wbgesstty_11_i           |
| 138 |          /family-entertainment-guide/disney-plus-picks/ls092677739/mediaviewer/rm3322936833?ref_=hm_edcep_wbgesstty_11_t           |
| 139 |                                                 feature/bornondate/?ref_=hm_brn_sm                                                 |
| 140 |                                                      /news/top/?ref_=hm_nw_sm                                                      |
| 141 |                                                 /news/ni63526960/?ref_=hm_nw_tp_1                                                  |
| 142 |                                                 /news/ni63526796/?ref_=hm_nw_tp_2                                                  |
| 143 |                                                 /news/ni63526795/?ref_=hm_nw_tp_3                                                  |
| 144 |                                                 /news/ni63526328/?ref_=hm_nw_tp_4                                                  |
| 145 |                                                 /news/ni63528799/?ref_=hm_nw_tp_5                                                  |
| 146 |                                                    /news/top/?ref_=hm_nw_tp_tb                                                     |
| 147 |                                                   /news/movie/?ref_=hm_nw_mv_tb                                                    |
| 148 |                                                     /news/tv/?ref_=hm_nw_tv_tb                                                     |
| 149 |                                                 /news/celebrity/?ref_=hm_nw_cel_tb                                                 |
| 150 | https://help.imdb.com/article/imdb/general-information/why-do-i-need-to-enable-my-cookies-on-imdb/GWE3JQ8VUQDCFW3Q?ref_=helpsrall# |
| 151 |                                                  https://slyb.app.link/SKdyQ6A449                                                  |
| 152 |                                                     https://facebook.com/imdb                                                      |
| 153 |                                                     https://instagram.com/imdb                                                     |
| 154 |                                                       https://twitch.tv/IMDb                                                       |
| 155 |                                                      https://twitter.com/imdb                                                      |
| 156 |                                                     https://youtube.com/imdb/                                                      |
| 157 |                                                  https://slyb.app.link/SKdyQ6A449                                                  |
| 158 |                                                     https://help.imdb.com/imdb                                                     |
| 159 |                     https://help.imdb.com/article/imdb/general-information/imdb-site-index/GNCX7BHNSPBTFALQ#so                     |
| 160 |                                        https://pro.imdb.com?ref_=cons_tf_pro&rf=cons_tf_pro                                        |
| 161 |                                                   https://www.boxofficemojo.com                                                    |
| 162 |                                                    https://developer.imdb.com/                                                     |
| 163 |                                             https://www.imdb.com/pressroom/?ref_=ft_pr                                             |
| 164 |                                      https://advertising.amazon.com/resources/ad-specs/imdb/                                       |
| 165 |                                               https://www.amazon.jobs/en/teams/imdb                                                |
| 166 |                                                      /conditions?ref_=ft_cou                                                       |
| 167 |                                                        /privacy?ref_=ft_pvc                                                        |
| 168 |                                             https://www.amazon.com/b/?&node=5160028011                                             |
+-----+------------------------------------------------------------------------------------------------------------------------------------+

```