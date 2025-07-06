import { Canvas } from "@react-three/fiber";
import { OrbitControls, Stars } from "@react-three/drei";

export default function ThreeBackground() {
    return (
        <Canvas
            style={{ position: "absolute", top: 0, left: 0, zIndex: 0 }}
            camera={{ position: [0, 0, 1], fov: 75 }}
        >
      <ambientLight intensity={0.5} />
      <pointLight position={[10, 10, 10]} />
      <Stars radius={80} depth={50} count={10000} factor={2} saturation={0} fade speed={1} />
      <OrbitControls enableZoom={false} enablePan={false} enableRotate={false} />
    </Canvas>
    );
}