{
  description = "Ambiente di Sviluppo Isolato OGA VGEN con Just Task Runner";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        pythonEnv = pkgs.python313.withPackages (ps: [
          ps.manim
          ps.edge-tts
          ps.numpy
          ps.ruff
          ps.mypy
	  ps.mutagen
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = [
            pythonEnv
            pkgs.ffmpeg
            pkgs.just # Aggiunto come standard di automazione del team
	    pkgs.yt-dlp
          ];

          shellHook = ''
            export PYTHONDONTWRITEBYTECODE=1
            export PYTHONUNBUFFERED=1
            echo "Digita 'just' per formattare, controllare e compilare il video"
          '';
        };
      });
}
