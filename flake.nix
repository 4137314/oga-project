{
  description = "Ambiente di sviluppo isolato per presentazioni Beamer LaTeX e Video TTS";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
      
      # Distribuzione TeX Live solida e onnicomprensiva
      texEnvironment = pkgs.texlive.combine {
        inherit (pkgs.texlive) 
          scheme-small
          collection-latexextra # Include automaticamente Metropolis, Owl e tutti i macro package extra
          booktabs         
          microtype        
          pgfplots         
          etoolbox
          translator;
      };

      # Ambiente Python isolato con gTTS incluso
      pythonEnv = pkgs.python3.withPackages (ps: with ps; [
        edge-tts
	rich
      ]);
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          texEnvironment   
          pythonEnv        
          gnumake          
          pdfpc            
          poppler-utils    
          ffmpeg           
        ];
      };
    };
}
