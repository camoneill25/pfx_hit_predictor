CREATE TABLE pitches(
   dateStamp           DATE NULL
  ,park_sv_id          INTEGER NULL
  ,play_guid           VARCHAR NULL
  ,ab_total            INTEGER NULL
  ,ab_count            INTEGER NULL
  ,pitcher_id          INTEGER NULL
  ,batter_id           INTEGER NULL
  ,ab_id               INTEGER NULL
  ,des                 VARCHAR NULL
  ,pitch_type          VARCHAR NULL
  ,pitch_id            INTEGER NULL
  ,sz_top              FLOAT NULL
  ,sz_bot              FLOAT NULL
  ,pfx_xDataFile       FLOAT NULL
  ,pfx_zDataFile       FLOAT NULL
  ,mlbam_pitch_name    VARCHAR NULL
  ,zone_location       INTEGER NULL
  ,pitch_con           FLOAT NULL
  ,stand               VARCHAR NULL
  ,strikes             INTEGER NULL
  ,balls               INTEGER NULL
  ,p_throws            VARCHAR NULL
  ,gid                 PRIMARY KEY VARCHAR
  ,pdes                VARCHAR NULL
  ,spin                FLOAT NULL
  ,norm_ht             FLOAT NULL
  ,inning              INTEGER NULL
  ,pitcher_team        VARCHAR NULL
  ,tstart              FLOAT NULL
  ,vystart             FLOAT NULL
  ,ftime               FLOAT NULL
  ,pfx_x               FLOAT NULL
  ,pfx_z               FLOAT NULL
  ,uncorrected_pfx_x   FLOAT NULL
  ,uncorrected_pfx_z   FLOAT NULL
  ,x0                  FLOAT NULL
  ,y0                  INTEGER NULL
  ,z0                  FLOAT NULL
  ,vx0                 FLOAT NULL
  ,vy0                 FLOAT NULL
  ,vz0                 FLOAT NULL
  ,ax                  FLOAT NULL
  ,ay                  FLOAT NULL
  ,az                  FLOAT NULL
  ,start_speed         FLOAT NULL
  ,px                  FLOAT NULL
  ,pz                  FLOAT NULL
  ,pxold               FLOAT NULL
  ,pzold               FLOAT NULL
  ,tm_spin             INTEGER NULL
  ,sb                  INTEGER NULL
);

CREATE TABLE batters(
  fg_id            PRIMARY KEY INTEGER
  name             VARCHAR
  team             VARCHAR
  G                INTEGER
  AB               INTEGER
  H                INTEGER
  1B               INTEGER
  2B               INTEGER
  3B               INTEGER
  HR               INTEGER
  RBI              INTEGER
  BB               INTEGER
  SO               INTEGER
  AVG              FLOAT
  OBP              FLOAT
  SLG              FLOAT
  OPS              FLOAT
  player_id        FOREIGN KEY INTEGER
);
