%global         majorminor      1.0
%global         gst_mm          gstreamer-%{majorminor}

Name:            gstreamer1-plugins-base
Version:         1.14.4
Release:         2
Summary:         GStreamer streaming media framework base plugins
License:         LGPLv2+
URL:             http://gstreamer.freedesktop.org/
Source0:         http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz

Patch0:         0001-missing-plugins-Remove-the-mpegaudioversion-field.patch
Patch6000:      CVE-2019-9928.patch

BuildRequires:  gcc-c++ gstreamer1-devel >= %{version} gobject-introspection-devel >= 1.31.1 iso-codes-devel alsa-lib-devel
BuildRequires:  cdparanoia-devel libogg-devel >= 1.0 libtheora-devel >= 1.1 libvisual-devel libvorbis-devel >= 1.0 libXv-devel
BuildRequires:  orc-devel >= 0.4.18 pango-devel pkgconfig opus-devel gtk-doc >= 1.3 libxslt
BuildRequires:  automake gettext-devel libtool chrpath mesa-libGL-devel mesa-libGLES-devel mesa-libGLU-devel mesa-libEGL-devel wayland-devel

Requires:       iso-codes

Conflicts: gstreamer1-plugins-bad-free < 1.13

%description
GStreamer is a graphics library for built-in media processing components. BasePlug-ins is a the collections used to maintain the GStreamer plugin.

%package devel
Summary:        GStreamer Base Plugins Development files
Requires:       %{name} = %{version}-%{release}
Provides:       tools
Obsoletes:      tools

%description devel
This package contains static libraries and header files.

%package help
Summary:        Developer documentation for GStreamer Base plugins library
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
Provides:       devel-docs
Obsoletes:      devel-docs

%description help
This package provides manual for developpers.

%prep
%setup -q -n gst-plugins-base-%{version}
%patch0 -p1
%patch6000 -p1

%build
NOCONFIGURE=1 \
./autogen.sh

%configure \
  --with-package-name='GStreamer-plugins-base package' --enable-experimental \
  --disable-fatal-warnings --disable-silent-rules --enable-gtk-doc --enable-orc

%make_build V=1

%install
%make_install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/gstreamer-base.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2013 Richard Hughes <richard@hughsie.com> -->
<component type="codec">
  <id>gstreamer-base</id>
  <metadata_license>CC0-1.0</metadata_license>
  <name>GStreamer Multimedia Codecs - Base</name>
  <summary>Multimedia playback for Ogg, Theora and Vorbis</summary>
  <description>
    <p>
      This addon includes system codecs that are essential for the running system.
    </p>
    <p>
      A codec decodes audio and video for for playback or editing and is also
      used for transmission or storage.
      Different codecs are used in video-conferencing, streaming media and
      video editing applications.
    </p>
  </description>
  <keywords>
    <keyword>Ogg</keyword>
    <keyword>Theora</keyword>
    <keyword>Vorbis</keyword>
  </keywords>
  <compulsory_for_desktop>GNOME</compulsory_for_desktop>
  <url type="homepage">http://gstreamer.freedesktop.org/</url>
  <url type="bugtracker">https://bugzilla.gnome.org/enter_bug.cgi?product=GStreamer</url>
  <url type="donation">http://www.gnome.org/friends/</url>
  <url type="help">http://gstreamer.freedesktop.org/documentation/</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%find_lang gst-plugins-base-%{majorminor}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'

%ldconfig_scriptlets

%files -f gst-plugins-base-1.0.lang
%license COPYING
%{_datadir}/appdata/*.appdata.xml
%{_libdir}/libgst*
%{_libdir}/girepository-1.0/Gst*
%{_libdir}/%{gst_mm}/libgst*

%files devel
%{_bindir}/gst-*

%dir %{_includedir}/%{gst_mm}/gst/allocators
%{_includedir}/%{gst_mm}/gst/allocators/allocators.h
%{_includedir}/%{gst_mm}/gst/allocators/allocators-prelude.h
%{_includedir}/%{gst_mm}/gst/allocators/gstdmabuf.h
%{_includedir}/%{gst_mm}/gst/allocators/gstfdmemory.h
%{_includedir}/%{gst_mm}/gst/allocators/gstphysmemory.h
%dir %{_includedir}/%{gst_mm}/gst/app
%{_includedir}/%{gst_mm}/gst/app/app.h
%{_includedir}/%{gst_mm}/gst/app/app-prelude.h
%{_includedir}/%{gst_mm}/gst/app/app-enumtypes.h
%{_includedir}/%{gst_mm}/gst/app/gstappsink.h
%{_includedir}/%{gst_mm}/gst/app/gstappsrc.h
%dir %{_includedir}/%{gst_mm}/gst/audio
%{_includedir}/%{gst_mm}/gst/audio/audio-channels.h
%{_includedir}/%{gst_mm}/gst/audio/audio-channel-mixer.h
%{_includedir}/%{gst_mm}/gst/audio/audio-converter.h
%{_includedir}/%{gst_mm}/gst/audio/audio-format.h
%{_includedir}/%{gst_mm}/gst/audio/audio-info.h
%{_includedir}/%{gst_mm}/gst/audio/audio-enumtypes.h
%{_includedir}/%{gst_mm}/gst/audio/audio-quantize.h
%{_includedir}/%{gst_mm}/gst/audio/audio-resampler.h
%{_includedir}/%{gst_mm}/gst/audio/audio.h
%{_includedir}/%{gst_mm}/gst/audio/audio-prelude.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudioaggregator.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiobasesink.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiobasesrc.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiocdsrc.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudioclock.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiodecoder.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudioencoder.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiofilter.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudioiec61937.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiometa.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudioringbuffer.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiosink.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiosrc.h
%{_includedir}/%{gst_mm}/gst/audio/gstaudiostreamalign.h
%{_includedir}/%{gst_mm}/gst/audio/streamvolume.h
%dir %{_includedir}/%{gst_mm}/gst/fft
%{_includedir}/%{gst_mm}/gst/fft/fft.h
%{_includedir}/%{gst_mm}/gst/fft/fft-prelude.h
%{_includedir}/%{gst_mm}/gst/fft/gstfft.h
%{_includedir}/%{gst_mm}/gst/fft/gstfftf32.h
%{_includedir}/%{gst_mm}/gst/fft/gstfftf64.h
%{_includedir}/%{gst_mm}/gst/fft/gstffts16.h
%{_includedir}/%{gst_mm}/gst/fft/gstffts32.h
%{_includedir}/%{gst_mm}/gst/gl/
%{_libdir}/%{gst_mm}/include/gst/gl/
%dir %{_includedir}/%{gst_mm}/gst/pbutils
%{_includedir}/%{gst_mm}/gst/pbutils/codec-utils.h
%{_includedir}/%{gst_mm}/gst/pbutils/descriptions.h
%{_includedir}/%{gst_mm}/gst/pbutils/encoding-profile.h
%{_includedir}/%{gst_mm}/gst/pbutils/encoding-target.h
%{_includedir}/%{gst_mm}/gst/pbutils/gstaudiovisualizer.h
%{_includedir}/%{gst_mm}/gst/pbutils/gstdiscoverer.h
%{_includedir}/%{gst_mm}/gst/pbutils/gstpluginsbaseversion.h
%{_includedir}/%{gst_mm}/gst/pbutils/install-plugins.h
%{_includedir}/%{gst_mm}/gst/pbutils/missing-plugins.h
%{_includedir}/%{gst_mm}/gst/pbutils/pbutils-enumtypes.h
%{_includedir}/%{gst_mm}/gst/pbutils/pbutils.h
%{_includedir}/%{gst_mm}/gst/pbutils/pbutils-prelude.h
%dir %{_includedir}/%{gst_mm}/gst/riff
%{_includedir}/%{gst_mm}/gst/riff/riff.h
%{_includedir}/%{gst_mm}/gst/riff/riff-prelude.h
%{_includedir}/%{gst_mm}/gst/riff/riff-ids.h
%{_includedir}/%{gst_mm}/gst/riff/riff-media.h
%{_includedir}/%{gst_mm}/gst/riff/riff-read.h
%dir %{_includedir}/%{gst_mm}/gst/rtp
%{_includedir}/%{gst_mm}/gst/rtp/gstrtcpbuffer.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtpbaseaudiopayload.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtpbasedepayload.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtpbasepayload.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtpbuffer.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtpdefs.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtp-enumtypes.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtphdrext.h
%{_includedir}/%{gst_mm}/gst/rtp/gstrtppayloads.h
%{_includedir}/%{gst_mm}/gst/rtp/rtp.h
%{_includedir}/%{gst_mm}/gst/rtp/rtp-prelude.h
%dir %{_includedir}/%{gst_mm}/gst/rtsp
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtsp.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtsp-enumtypes.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtspconnection.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtspdefs.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtspextension.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtspmessage.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtsprange.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtsptransport.h
%{_includedir}/%{gst_mm}/gst/rtsp/gstrtspurl.h
%{_includedir}/%{gst_mm}/gst/rtsp/rtsp.h
%{_includedir}/%{gst_mm}/gst/rtsp/rtsp-prelude.h
%dir %{_includedir}/%{gst_mm}/gst/sdp
%{_includedir}/%{gst_mm}/gst/sdp/gstsdp.h
%{_includedir}/%{gst_mm}/gst/sdp/gstsdpmessage.h
%{_includedir}/%{gst_mm}/gst/sdp/gstmikey.h
%{_includedir}/%{gst_mm}/gst/sdp/sdp.h
%{_includedir}/%{gst_mm}/gst/sdp/sdp-prelude.h
%dir %{_includedir}/%{gst_mm}/gst/tag
%{_includedir}/%{gst_mm}/gst/tag/gsttagdemux.h
%{_includedir}/%{gst_mm}/gst/tag/gsttagmux.h
%{_includedir}/%{gst_mm}/gst/tag/tag.h
%{_includedir}/%{gst_mm}/gst/tag/tag-prelude.h
%{_includedir}/%{gst_mm}/gst/tag/tag-enumtypes.h
%{_includedir}/%{gst_mm}/gst/tag/xmpwriter.h
%dir %{_includedir}/%{gst_mm}/gst/video
%{_includedir}/%{gst_mm}/gst/video/colorbalance.h
%{_includedir}/%{gst_mm}/gst/video/colorbalancechannel.h
%{_includedir}/%{gst_mm}/gst/video/gstvideoaffinetransformationmeta.h
%{_includedir}/%{gst_mm}/gst/video/gstvideodecoder.h
%{_includedir}/%{gst_mm}/gst/video/gstvideoencoder.h
%{_includedir}/%{gst_mm}/gst/video/gstvideofilter.h
%{_includedir}/%{gst_mm}/gst/video/gstvideometa.h
%{_includedir}/%{gst_mm}/gst/video/gstvideopool.h
%{_includedir}/%{gst_mm}/gst/video/gstvideosink.h
%{_includedir}/%{gst_mm}/gst/video/gstvideotimecode.h
%{_includedir}/%{gst_mm}/gst/video/gstvideoutils.h
%{_includedir}/%{gst_mm}/gst/video/navigation.h
%{_includedir}/%{gst_mm}/gst/video/video-blend.h
%{_includedir}/%{gst_mm}/gst/video/video-overlay-composition.h
%{_includedir}/%{gst_mm}/gst/video/video-chroma.h
%{_includedir}/%{gst_mm}/gst/video/video-color.h
%{_includedir}/%{gst_mm}/gst/video/video-converter.h
%{_includedir}/%{gst_mm}/gst/video/video-dither.h
%{_includedir}/%{gst_mm}/gst/video/video-enumtypes.h
%{_includedir}/%{gst_mm}/gst/video/video-event.h
%{_includedir}/%{gst_mm}/gst/video/video-format.h
%{_includedir}/%{gst_mm}/gst/video/video-frame.h
%{_includedir}/%{gst_mm}/gst/video/video-info.h
%{_includedir}/%{gst_mm}/gst/video/video-multiview.h
%{_includedir}/%{gst_mm}/gst/video/video-resampler.h
%{_includedir}/%{gst_mm}/gst/video/video-scaler.h
%{_includedir}/%{gst_mm}/gst/video/video-tile.h
%{_includedir}/%{gst_mm}/gst/video/video.h
%{_includedir}/%{gst_mm}/gst/video/video-prelude.h
%{_includedir}/%{gst_mm}/gst/video/videodirection.h
%{_includedir}/%{gst_mm}/gst/video/videoorientation.h
%{_includedir}/%{gst_mm}/gst/video/videooverlay.h

%dir %{_datadir}/gst-plugins-base/%{majorminor}/
%{_datadir}/gst-plugins-base/%{majorminor}/license-translations.dict
%{_datadir}/gir-1.0/Gst*.gir

%{_libdir}/pkgconfig/*.pc

%files help
%doc AUTHORS README REQUIREMENTS
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-libs-%{majorminor}
%doc %{_datadir}/gtk-doc/html/gst-plugins-base-plugins-%{majorminor}
%{_mandir}/man1/gst-discoverer-*.gz
%{_mandir}/man1/gst-play-*.gz
%{_mandir}/man1/gst-device-monitor-*.gz

%changelog
* Sat Dec 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.14.4-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:bugfix about configure

* Mon Sep 16 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.14.4-1
- Package init
